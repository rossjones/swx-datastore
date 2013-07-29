import os
import sys
import time
import pwd
import grp
import optparse
import logging

from dataproxy import ProxyHandler, ProxyHTTPServer

def run_server():

    parser = optparse.OptionParser()
    parser.add_option("--setuid", action="store_true")
    parser.add_option("--pidfile")
    parser.add_option("--logfile")
    parser.add_option("--daemonize")
    parser.add_option("--toaddrs", default="")
    options, pargs = parser.parse_args()

    # daemon mode
    if options.daemonize:
        if os.fork() == 0 :
            os.setsid()
            sys.stdin = open('/dev/null')
            if os.fork() == 0 :
                ppid = os.getppid()
                while ppid != 1 :
                    time.sleep(1)
                    ppid = os.getppid()
            else :
                os._exit (0)
        else :
            os.wait()
            sys.exit (1)

    pf = open(options.pidfile or "/tmp/swx_datastore.pid", 'w')
    pf.write('%d\n' % os.getpid())
    pf.close()

    if options.setuid:
        gid = grp.getgrnam("nogroup").gr_gid
        os.setregid(gid, gid)
        uid = pwd.getpwnam("nobody").pw_uid
        os.setreuid(uid, uid)

    #logging.config.fileConfig(configfile)

    port = 5009 #config.getint('dataproxy', 'port')
    ProxyHandler.protocol_version = "HTTP/1.0"
    httpd = ProxyHTTPServer(('', port), ProxyHandler)
    httpd.max_children = 160
    sa = httpd.socket.getsockname()

    logger = logging.getLogger('dataproxy')

    logger.info("Serving HTTP on %s port %s" %(sa[0], sa[1]))

    httpd.serve_forever()

