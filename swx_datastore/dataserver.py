# -*- coding: utf-8 -*-
"""
Replacement server for the dataproxy

Based on server from Guillaume Aubert (gaubert) at zeromq.org
"""

import datalib

import signal
import sys
import time
import threading
import zmq


def read_socket(sock):
    # TODO: Really want a blocking read here.
    try:
        return sock.recv()
    except Exception, e:
        print e

def worker_routine(worker_url, context):
    socket = context.socket(zmq.REP)
    socket.connect(worker_url)

    # Do ident dance
    print "Awaiting first connection"
    query  = read_socket(socket)

    # Connect to DB via datalib
    with datalib.SQLiteDatabase(context, "","short", "auth", "id", "attachables") as db:

        while True:
            query  = read_socket(socket)
            print "Received request: [%s]\n" % (query)
            # convert request to JSON

            # encode query as json before asking datalib to process
            response = db.process("")

            # send reply back to client
            json.dump(res, socket)
            socket.send('\n')


def signal_handler(signal, frame):
    global clients
    global workers
    global context

    print "CTRL-C caught"
    if clients: clients.close()
    if workers: workers.close()
    if context: context.term()

    sys.exit(0)


clients = None
workers = None
context = None

def run_server(threads=10):
    """ server routine """
    signal.signal(signal.SIGINT, signal_handler)

    global clients
    global workers
    global context

    url_worker = "inproc://workers"
    url_client = "tcp://*:2112"

    context = zmq.Context(1)
    clients = context.socket(zmq.ROUTER)
    clients.bind(url_client)

    # Worker sockets
    workers = context.socket(zmq.DEALER)
    workers.bind(url_worker)

    for i in range(threads):
        thread = threading.Thread(target=worker_routine, args=(url_worker, context, ))
        thread.setDaemon(True)
        thread.start()

    zmq.device(zmq.QUEUE, clients, workers)

