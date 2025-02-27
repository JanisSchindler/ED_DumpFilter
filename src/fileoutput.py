# Dumps the accepted lines into a new file.
class FileOutput: 
  
  def initialize(self, path):
     self.output = open(path, "w")
     self.output.write("[" + "\n")

  def onAccepted(self, line):
   self.output.write(line + "\n")

  def close(self):
    self.output.write("]")
    self.output.close()