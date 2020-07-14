from multiprocessing.connection import Client

address = ('localhost', 6000)
conn = Client(address, authkey='secret password')
#conn.send('close')
while True:
	conn.send("say hello")
# can also send arbitrary objects:
# conn.send(['a', 2.5, None, int, sum])
conn.close()