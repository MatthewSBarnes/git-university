import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999

# connection to hostname on the port.
s.connect((host, port))

# Receive no more than 1024 bytes
# Fundamentally this line of code is problematic, because you're just buffering in 1024 bytes.  
msg = s.recv(1024)                                     

s.close()

print (msg.decode('ascii'))
