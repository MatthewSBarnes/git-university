class packet:
  def __init__ (self, source, destination):
    self.source = source
    self.destination = destination

  def Display (self):
    print (bin(self.source))
    print (bin(self.destination))
