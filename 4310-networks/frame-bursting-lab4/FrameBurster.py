import random
import binascii
import lab4
import sys

#set up our byte arrays
def mactobinar(mac):
  return binascii.unhexlify(mac.replace(':', ''))
  #source and destination addresses aren't actually important, but I stole them 
  # from http://accc.uic.edu/answer/what-my-ip-address-mac-address

def genpacket(): 
  #packet Generator, source and destination mac addresses are hard coded.  
  sourcemac = "00:15:E9:2B:99:3C"
  source = mactobinar(sourcemac)
  destmac="00:09:3D:12:33:33"
  destination = mactobinar(destmac)
  # a byte array is what it sounds like, and array of bytes, it's basically a 
  # string but you have to decide how to interpret it
  data = bytearray() #creates an empty bytearray
  sizeofdata = random.randint(46,1500) 
  # this generates a random integer for the data payload of between 
  # 46 and 1500 bytes
  #sizeofdata = random.randint(3,7) 
  #same as above but smaller for manual debugging/reading
  #print(sizeofdata) 
  #this will tell you how big the (randomly) sized packet you made is
  for x in range (0, sizeofdata):
    data.append(random.randint(0,255))
  return lab4.DIXFrame(source, destination, data) 
  # Note that our packet has some stuff to construct the CRC of 
  # the packet as well as the type
#print(data) 
# printing the data is not highly recommended, as you get basically garbled 
#  bytes in ascii in formats like \xx when it can't convert to ascii, or 
#  the actual ascii character. That isn't all that important.  

#generate two packets
pack1 = genpacket()
pack2 = genpacket()

# Because bye arrays appear to be passed by reference, and are uncooperative 
#  about joining/appending etc. this is the easiest way to get data from two 
#  packets into one new one.  

data2 = bytearray()
for y in pack1.data:
  data2.append(y)
for z in pack2.data:
  data2.append(z)

#Handy stuff for printing out the state of memory etc. 
#  (since we don't have a debugger)

# print(data2)	 
print(len(pack1.data))
print(len(pack2.data))

#instructions
# Generate some packets with a source and data of various sizes 
#  (from 46-1500 bytes), and with a checksum
# If it's less than 512 bytes
#   strip off the source, dest, type and checksum
#   keep ripping apart packets until you have enough data to make a 512 byte
#   frame, but not more than 1518 (note that 512 and 1518 includes a header 
#   and crc, which total 18 bytes)
#   Assemble the new frame
# else 
#   delete the packet (or send it, if we had a network to send it on)

pack_one_source = pack1.source
pack_one_dest = pack1.dest

data_array = bytearray()

if (len(pack1.data) < 512):
  while (sys.getsizeof(data_array) < 512):
    print("    Appending packet.data: " + str(len(pack1.data)))
    for y in pack1.data:
      data_array.append(y)
    pack1 = genpacket() 
    print("Generating new packet...\n")
   
pack3=lab4.DIXFrame(pack_one_source, pack_one_dest, data_array)
 
pack_two_source = pack2.source
pack_two_dest = pack2.dest

data_array2 = bytearray()

if (len(pack2.data) < 512):
  while (sys.getsizeof(data_array2) < 512):
    print("    Appending packet.data: " + str(len(pack2.data)))
    for y in pack2.data:
      data_array2.append(y)
    pack2 = genpacket() 
    print("Generating new packet...\n")

pack4 = lab4.DIXFrame(pack_two_source, pack_two_dest, data_array2)  

if (len(pack3.data) > 0):
  print("\n\nNew packet, pack3 len(pack3.data): " + str(len(pack3.data)))
else:
  print("\n\nNo new packet 3, packet 1 is larger than 512 bytes")


if (len(pack4.data) > 0):
  print("New packet, pack4 len(pack4.data): " + str(len(pack4.data)))
else:
  print("No new packet 4, packet 1 is larger than 512 bytes")
