import systemparser

# Calls onAccepted for systems that are within maxDistance of origin
def filter (input, onAccepted, maxDistanceSquared, origin):

    coords = systemparser.getcoords(input)
    if (coords == None):
       return
    
    if (checkSquaredDistance(coords.X, coords.Y, coords.Z, maxDistanceSquared, origin) == False):
        return
        
    onAccepted()
    return

def checkSquaredDistance(x,y,z, maxDistanceSquared, origin):
       # Distance is Sqrt(deltaX ^2 + deltaY ^2 + deltaZ^2)
       # To prevent the calculation of the square root each time the squared distance is used
       deltaX = origin.X - x
       deltaY = origin.Y - y
       deltaZ = origin.Z - z
       distanceSquared = deltaX * deltaX + deltaY * deltaY + deltaZ * deltaZ
       return distanceSquared < maxDistanceSquared

    