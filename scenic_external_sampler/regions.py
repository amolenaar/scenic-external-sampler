from scenic.core.regions import RectangularRegion

NorthEast = RectangularRegion(position=(50, 50), heading=0.0, width=100, length=100, name="NorthEast")
NorthWest = RectangularRegion(position=(-50, 50), heading=0.0, width=100, length=100, name="NorthWest")
SouthEast = RectangularRegion(position=(50, -50), heading=0.0, width=100, length=100, name="SouthEast")
SouthWest = RectangularRegion(position=(-50, -50), heading=0.0, width=100, length=100, name="SouthWest")
