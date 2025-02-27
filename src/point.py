class Point:
  X : float
  Y : float
  Z : float

  def __init__(self, x, y, z):
    self.X = x
    self.Y = y
    self.Z = z

  @classmethod
  def fromCoordinates(cls, x, y, z):
    X = float(x)
    Y = float(y)
    Z = float(z)
    return cls(x, y, z)
    
  @classmethod
  def fromArgument(cls, argument):
    elements = argument.split("|")

    x = float(elements[0])
    y = float(elements[1])
    z = float(elements[2])
    return cls(x, z, y)

