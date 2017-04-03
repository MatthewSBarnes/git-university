import socket
import hashlib
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #TCP: socket.SOCK_STREAM

# get local machine name
host = socket.gethostname()                           

port = 9999

# TCP connection to hostname on the port.
#s.connect((host, port))                               

# hash stuff.

#UDP way, just send some data
msg = "asjkdfhlaskdjfh"
msg2 = b"asjkdfhlaskdjfh"

hashish = hashlib.sha224(msg2).hexdigest()

sent = s.sendto(msg.encode('ascii'), (host, port))

sent = s.sendto(hashish.encode('ascii'), (host, port))

# Receive no more than 1024 bytes
# Fundamentally this line of code is problematic, because you're just buffering in 1024 bytes.  
msg = s.recv(1024)                                     

s.close()

print (msg.decode('ascii'))
