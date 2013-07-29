import subprocess
import time

server_process = None

def setup_module():
    global server_process
    server_process = subprocess.Popen("datastore")
    time.sleep(0.25)

def teardown_module():
    global server_process
    if server_process:
        server_process.kill()