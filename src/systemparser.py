from point import Point
import re

def getcoords(line):
    x = 0.0
    y = 0.0
    z = 0.0

    # Sample line:
    # {"id64":11369639,"name":"CPD-59 2591","mainStar":"O (Blue-White) Star","coords":{"x":7841.34375,"y":-107.78125,"z":2486.96875},"updateTime":"2025-02-25 20:45:07+00"},	
    # Regex reads numbers that come after "x":, "y": and "z":
    result = re.findall(r"\"[xyz]\"\:([-+]?\d*\.\d+|\d+)", line)
    if (len(result) != 3):
        return None

    x = float(result[0])
    y = float(result[1])
    z = float(result[2])
   
    p = Point.fromCoordinates(x, y, z)    
    return p