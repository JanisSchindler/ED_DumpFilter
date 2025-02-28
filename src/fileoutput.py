# Dumps the accepted lines into a new file.
class FileOutput: 
  
  def initialize(self, path):
     self.output = open(path, "wb")
     self.output.write(b"[")

  def onAccepted(self, lineBytes):
   self.output.write(b"\n")
   self.output.write(lineBytes)
   return

  def close(self):
    self.output.write(b"]")
    self.output.close()