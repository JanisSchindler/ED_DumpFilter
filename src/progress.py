import sys

# Prints the current progress to the output
class Progress:
  size: int
  currentStep: int
 
  def __init__(self, size):
    self.size = size
    self.currentStep = 0
    print("Starting...")

  def onprogress(self, processed):
    progress = int(processed / self.size * 1000)
    
    # print a message once new percentage is reached, for 100 steps total at maximum
    if (progress <= self.currentStep):
      return

    self.currentStep = progress

    # Putting \r at the end resets the cursor to the start of the line.
    # So that the next call overwrites the progress.
    print("..." + f"{progress/10}" + "%", end='\r')

    if (progress >= 1000):
      print("...done               ")