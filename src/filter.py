from systemparser import SystemParser
import orjson

class Filter:
  def __init__(self, columns):
    self.columns = columns
    self.parser = SystemParser()

  # Calls onAccepted for systems that are within maxDistance of origin
  def filter (self, input, onAccepted, maxDistanceSquared, origin):
    coords = self.parser.getcoords(input)
    if (coords == None):
       return
    
    if (self.checkSquaredDistance(coords, maxDistanceSquared, origin) == False):
        return
    
    cropped = self.cropcolumns(input)  
    onAccepted(cropped)
    return
  
  def cropcolumns(self, line):
    record = orjson.loads(line.strip(" \n\t,"))
    cropped = {k: v for k,v in record.items() if k in self.columns}
    return orjson.dumps(cropped)

  def checkSquaredDistance(self, coords, maxDistanceSquared, origin):
    # Distance is Sqrt(deltaX ^2 + deltaY ^2 + deltaZ^2)
    # To prevent the calculation of the square root each time the squared distance is used
    deltaX = origin.X - coords.X
    deltaY = origin.Y - coords.Y
    deltaZ = origin.Z - coords.Z
    distanceSquared = deltaX * deltaX + deltaY * deltaY + deltaZ * deltaZ
    return distanceSquared < maxDistanceSquared