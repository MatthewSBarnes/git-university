import binascii


class DIXFrame:
  type= 0x0800 
  # this is the type for an IPv4 Frame, 0x86DD is IPv6, 
  # http://www.iana.org/assignments/ieee-802-numbers/ieee-802-numbers.xhtml \
  # ieee-802-numbers-1 has the full list of supported ethertypes, 
  # but it doesn't matter to us
	

  def __init__ (self, Source, Dest, Data):
    self.source=Source
    self.dest=Dest
    self.data=Data
    self.crc=binascii.crc32(Source+Dest+Data)
		

		
