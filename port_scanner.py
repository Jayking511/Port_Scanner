import pyfiglet
print(pyfiglet.figlet_format("port scanner".upper()))
import socket
import time
import threading
from queue import Queue

socket.setdefaulttimeout(0.25)
lock=threading.Lock()
ipaddr=input('IP Address: ')
host=socket.gethostbyname(ipaddr)
print('Scanning on IP Address: ',host)

def scan(port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        connection=s.connect((host,port))
        with lock:
            print(port, 'is open')
        connection.close()
    except Exception as e:
        pass
def execute():
    while True:
        w=q.get()
        scan(w)
        q.task_done()
q=Queue()
st_time=time.time()
for i in range(6535):
    t=threading.Thread(target=execute)
    t.daemon=True
    t.start()
for j in range(1,65535):
    q.put(j)
q.join()
print('Time taken:',time.time()-st_time)
