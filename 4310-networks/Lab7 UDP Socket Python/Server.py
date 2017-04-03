import socket    
import hashlib                                     
import hmac

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_DGRAM)  # rather than socket.SOCK_DGRAM TCP is SOCK_STREAM like last lab
# get local machine name
host = socket.gethostname()                           
port = 9999                                           
# bind to the port
serversocket.bind((host, port))                                  
# queue up to 5 requests
#serversocket.listen(5)         
msg = "UDP connection made"                                  
msg2 = msg + " and hacked!"                                
while True:
    # TCP Way establish a connection 
    #clientsocket,addr = serversocket.accept()      
    #print("Got a connection from %s" % str(addr))
	#msg='Thank you for connecting'+ "\r\n"
    #clientsocket.send(msg.encode('ascii'))
    #clientsocket.close()
	
	#the UDP way
	data, address = serversocket.recvfrom(4096)
	data = data.decode('ascii')
        
	hashmsg, address = serversocket.recvfrom(4096)
	hashmsg = data.decode('ascii')
	if hashmsg != hashlib.sha256(data).hexdigest():
		sent = serversocket.sendto(msg.encode('ascii'), address)
	else:	
		sent = serversocket.sendto(msg2.encode('ascii'), address)
