# Dumps the accepted lines into a new file.
class FileOutput: 
  
  def initialize(self, path):
    self.output = open(path, "wb")
    self.output.write(b"[")
    self.isFirstLine = True

  def onAccepted(self, lineBytes):
   # write a comma before the new line except in the first line
    if (self.isFirstLine == False):
      self.output.write(b",")

    self.isFirstLine = False     
    self.output.write(b"\n")
    self.output.write(b"\t")
    self.output.write(lineBytes)
    return

  def close(self):
    self.output.write(b"\n")
    self.output.write(b"]")
    self.output.close()