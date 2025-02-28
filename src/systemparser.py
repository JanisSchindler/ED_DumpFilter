from point import Point
import re

class SystemParser:

  def __init__(self):

    # Sample line:
    # {"id64":11369639,"name":"CPD-59 2591","mainStar":"O (Blue-White) Star","coords":{"x":7841.34375,"y":-107.78125,"z":2486.96875},"updateTime":"2025-02-25 20:45:07+00"},	
    # Regex isolates the coords part "x":7841.34375,"y":-107.78125,"z":2486.96875
    self.compiled_regex_filter = re.compile(r".*?(\"[xyz]\"\:([-+]?\d*\.\d+|\d+),?){3}")

    # Regex parses the coords and stores the numbers in the result list
    self.compiled_regex_coords = re.compile(r"\"[xyz]\"\:([-+]?\d*\.\d+|\d+)")

  def getcoords(self, line):
    match = self.compiled_regex_filter.match(line)
    if match:
      content = match.group()
      result =  self.compiled_regex_coords.findall(content)
      if (len(result) != 3):
        return None
      
      x = float(result[0])
      y = float(result[1])
      z = float(result[2])
   
      p = Point.fromCoordinates(x, y, z)    
      return p