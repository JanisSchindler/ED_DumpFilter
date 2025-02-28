from systemparser import SystemParser

class Filter:
  def __init__(self):
    self.columns = ["id64","name","coords",
                    "population","allegiance","government",
                    "primaryEconomy","secondaryEconomy","security",
                    "controllingPower","powerState"]

  parser = SystemParser()

  # Calls onAccepted for systems that are within maxDistance of origin
  def filter (self, input, onAccepted, maxDistanceSquared, origin):
    coords = self.parser.getcoords(input)
    if (coords == None):
       return
    
    if (checkSquaredDistance(coords.X, coords.Y, coords.Z, maxDistanceSquared, origin) == False):
        return
    
    cropped = self.parser.cropcolumns(input, self.columns)  
    onAccepted(cropped)
    return

def checkSquaredDistance(x,y,z, maxDistanceSquared, origin):
       # Distance is Sqrt(deltaX ^2 + deltaY ^2 + deltaZ^2)
       # To prevent the calculation of the square root each time the squared distance is used
       deltaX = origin.X - x
       deltaY = origin.Y - y
       deltaZ = origin.Z - z
       distanceSquared = deltaX * deltaX + deltaY * deltaY + deltaZ * deltaZ
       return distanceSquared < maxDistanceSquared

    