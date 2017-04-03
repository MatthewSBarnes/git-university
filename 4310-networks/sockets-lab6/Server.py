import socket                                         
import time
import threading

class myThread (threading.Thread):
  def __init__(self, sock):
    threading.Thread.__init__(self)
  def run(self):
    print ("Starting " + self.name)
    listen_socket(sock)	
    print ("Exiting " + self.name)


def create_socket():
  # create a socket object
  sock = socket.socket(
  	          socket.AF_INET, socket.SOCK_STREAM) 
  # get local machine name
  host = socket.gethostname()                           
  port = 9999                                           
  # bind to the port
  print("creating socket")
  sock.bind((host, port))
  listen_socket(sock)

def listen_socket(sock):
  # queue up to 5 requests
  sock.listen(5)                                           
  while True:
    # establish a connection
    clientsocket,addr = sock.accept()      
    print("Got a connection from %s" % str(addr))
    msg='Thank you for connecting'+ "\r\n"
    clientsocket.send(msg.encode('ascii'))

    myThread(sock).start()
    time.sleep(5)    
    clientsocket.close()


create_socket()
