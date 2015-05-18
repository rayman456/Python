def rPolygonAngle(sides):
	return((sides - 2) * 180.0) / sides

sides = input("Enter the number of sides: ")
sides = int(sides)

print("The interior angle in degrees is:", end = ' ')
print(format(rPolygonAngle(sides), ".2f"), end = '.')
