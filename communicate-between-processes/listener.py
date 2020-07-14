from multiprocessing.connection import Listener
from time import sleep

address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
listener = Listener(address, authkey='secret password')
conn = listener.accept()
print 'connection accepted from', listener.last_accepted
i=0
while True:
    msg = conn.recv()
    # do something with msg
    if msg == 'close':
        conn.close()
        break
    elif msg == 'say hello':
    	print("hello world")
    i+=1
    print(str(i))
    sleep(1)
listener.close()