# Prints the current progress to the output
class Progress:
  size: int
  currentStep: int
 
  def __init__(self, size):
    self.size = size
    self.currentStep = 0
    print("Starting...")
    print("...0%")

  def onprogress(self, processed):
    progress = int(processed / self.size * 100)
    
    # print a message once new percentage is reached, for 100 steps total at maximum
    if (progress <= self.currentStep):
      return

    self.currentStep = progress
    print("..." + f'{progress}' + "%")