#!/usr/bin/python

ipv4 = "192.168.001.010"

numbers = list(map(int, octal.split('.')))

print (str(octal) + " becomes")
print( '2002:{:02x}{:02x}:{:02x}{:02x}::1/64'.format(*numbers))

ipv6 = "2002:C1A9:6301::1/64"

