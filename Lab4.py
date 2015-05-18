import math
class Cylinder:
	def __init__(self, radius = 1.0, height = 1.0):
		self.radius = float(radius)
		self.height = float(height)
	
	def getPerimeter(self):
		return 2.0 * math.pi * self.radius
	
	def getEndArea(self):
		return math.pi * (self.radius ** 2.0)
		
	def getSideArea(self):
		return self.height * self.getPerimeter()
	
	def getSurfaceArea(self):
		return self.getSideArea() + (2.0 * self.getEndArea())
		
	def getVolume(self):
		return self.height * self.getEndArea()

class Cylinder1:
	def __init__(self, radius = 1.0, height = 1.0):
		self.__radius = float(radius)
		self.__height = float(height)
	
	def getPerimeter(self):
		return 2.0 * math.pi * self.__radius
	
	def getEndArea(self):
		return math.pi * (self.__radius ** 2.0)
		
	def getSideArea(self):
		return self.__height * self.getPerimeter()
	
	def getSurfaceArea(self):
		return self.getSideArea() + (2.0 * self.getEndArea())
		
	def getVolume(self):
		return self.__height * self.getEndArea()
	
	def getRadius(self):
		return self.__radius
		
	def getHeight(self):
		return self.__height
		
	def setRadius(self, radius):
		self.__radius = radius
	
	def setHeight(self, height):
		self.__height = height

def main():
    bottle = Cylinder()
        
    bottle.radius = 4
    bottle.height = 8
    print("The radius and height of the bottle are: ", bottle.radius, " and ", bottle.height)
    print("The perimeter of the bottle end circle is", bottle.getPerimeter())
    print("The end circle area of the bottle is ", bottle.getEndArea())
    print("The side area of the bottle is ", bottle.getSideArea())
    print("The total surface of the bottle is ", bottle.getSurfaceArea())
    print("The volume of the bottle is ", bottle.getVolume())

def main1():
    bottle = Cylinder1(4, 8)
        
    bottle.setRadius(2)   #  Note the value is different from the previous test 
    bottle.setHeight(4)
    print("The radius and height of the bottle are: ", bottle.getRadius(), " and ", bottle.getHeight())
    print("The perimeter of the bottle end circle is", bottle.getPerimeter())
    print("The end circle area of the bottle is ", bottle.getEndArea())
    print("The side area of the bottle is ", bottle.getSideArea())
    print("The total surface of the bottle is ", bottle.getSurfaceArea())
    print("The volume of the bottle is ", bottle.getVolume())

main() 
main1()
