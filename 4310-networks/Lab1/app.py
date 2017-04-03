import sys, re, lab1

pattern = re.compile('[0-9][0-9]?[0-9]?.[0-9][0-9]?[0-9]?.[0-9][0-9]?[0-9]?.[0-9][0-9]?[0-9]?')

if (len(sys.argv) > 1):
  if (sys.argv[1] == "-help"):
    print("Usage: python3.6 app.py [Valid IP address] [Valid IP address]"
          "\nA valid IP address looks like so: #.#.#.#,"
          "\nwhere each # can be 0-255."
          "\nCommand line arguments are optional, valid addresses are required.\n")
    exit()
  #print(sys.argv) 
  if (pattern.match(sys.argv[1])):
    #print("Pattern Match")
    source = sys.argv[1]
  else:
    print("Please enter a valid IP address"
          "\nA valid IP address looks like so: #.#.#.#,"
          "\nwhere each # can be 0-255")
    exit()
else:
  #print("Please enter an IP [255.255.255.255]")
  user_input = input("Please enter an IP [255.255.255.255]: ") 
  if (pattern.match(user_input)):
    source = user_input
  else:
    print("Please enter a valid IP, exiting program\n")
    exit()
#source = "192.168.1.1"
source_octets = source.split(".")
print (source_octets)
it = iter(source_octets)
iSource = 0
iSource = (int(next(it))<<24)
iSource = iSource + (int(next(it))<<16)
iSource = iSource + (int(next(it))<<8)
iSource = iSource + int(next(it))

if (len(sys.argv) > 2):
  if (pattern.match(sys.argv[2])):
    #print("Pattern Match")
    destination = sys.argv[2]
  else:
    print("Please enter a valid IP address"
          "\nA valid IP address looks like so: #.#.#.#,"
          "\nwhere each # can be 0-255")
    exit()
else:
  #print("Please enter an IP [255.255.255.255]")
  user_input = input("Please enter an IP [255.255.255.255]: ") 
  if (pattern.match(user_input)):
    destination = user_input
  else:
    print("Please enter a valid IP, exiting program\n")
    exit()

#destination = "192.168.2.101"

destinationoctets = destination.split(".")
print (destinationoctets)
it = iter(destinationoctets)
iDestination = 0
iDestination = (int(next(it))<<24)
iDestination = iDestination + (int(next(it))<<16)
iDestination = iDestination + (int(next(it))<<8)
iDestination = iDestination + int(next(it))

packet1 = lab1.packet(iSource, iDestination)
packet1.Display()
print()
exit()

