import turtle

def circle(radius, cx = None, cy = None, color = "black", fill = False):
	wasDown = turtle.isdown()
	turtle.up()
	if cx is not None and cy is not None:
		turtle.setpos(cx, cy)
	turtle.sety(turtle.ycor() - radius)
	if wasDown:
		turtle.down()
	if fill:
		turtle.color(color, color)
		turtle.begin_fill()
	else:
		turtle.pencolor(color)
	turtle.circle(radius)
	if fill:
		turtle.end_fill()

def rectangle(length, width, x = None, y = None, color = "black", fill = False):
	wasDown = turtle.isdown()
	turtle.up()
	if x is not None and y is not None:
		turtle.setpos(x, y)
	if wasDown:
		turtle.down()
	if fill:
		turtle.color(color, color)
		turtle.begin_fill()
	else:
		turtle.pencolor(color)
	turtle.goto(turtle.xcor() + length, turtle.ycor())
	turtle.goto(turtle.xcor(), turtle.ycor() + width)
	turtle.goto(turtle.xcor() - length, turtle.ycor())
	turtle.goto(turtle.xcor(), turtle.ycor() - width)
	if fill:
		turtle.end_fill()

def polygon(side, numberSides, angle = None, xstart = None, ystart = None, color = "black", fill = False):
	if numberSides < 3:
		print("Invalid number of sides.")
		return
	wasDown = turtle.isdown()
	turtle.up()
	if xstart is not None and ystart is not None:
		turtle.setpos(xstart, ystart)
	if angle is not None:
		turtle.setheading(angle)
	if wasDown:
		turtle.down()
	if fill:
		turtle.color(color, color)
		turtle.begin_fill()
	else:
		turtle.pencolor(color)
	degrees = 180 - (((numberSides - 2) * 180.0) / numberSides)
	for x in range(0, numberSides):
		turtle.forward(side)
		turtle.left(degrees)
	if fill:
		turtle.end_fill()
	
def chessboard(xstart, ystart, side, color = "black", background = "white"):
	wasDown = turtle.isdown()
	turtle.up()
	turtle.setpos(xstart, ystart)
	if wasDown:
		turtle.down()
	turtle.pensize(3)
	polygon(side, 4, 0)
	turtle.pensize(1)
	colorToggle = True
	step = side / 8.0
	for y in range(0, 8):
		if y % 2 == 0:
			colorToggle = True
		else:
			colorToggle = False
		for x in range(0, 8):
			if colorToggle:
				polygon(step, 4, 0, xstart + (x * step), ystart + (y * step), color, True)
			else:
				polygon(step, 4, 0, xstart + (x * step), ystart + (y * step), background, True)
			colorToggle = not colorToggle
	
#helper function for bezier curves
def factoral(value):
	if value == 0:
		return 1
	total = value
	value -= 1
	while(value > 1):
		total *= value
		value -= 1
	return total

#Bezier curve function which can accept any number of points > 3
#Smooth determines how rough the curve is. Higher smooth = less rough, 1 = straight line
def bezier(smooth, x1, y1, x2, y2, x3, y3, *others):

	if len(others) % 2 != 0:
		print("Missing point data.")
		return
	if smooth < 1:
		print("Invalid smooth value")
		return
	wasDown = turtle.isdown()
	points = list(others)
	xval = [x1, x2, x3] + points[0:len(points):2]
	yval = [y1, y2, y3] + points[1:len(points):2]
	t, n, factn, step = 0, len(xval) - 1, factoral(len(xval) - 1), 1.0/smooth
	turtle.up()
	turtle.goto(x1, y1)
	if wasDown:
		turtle.down()
	while(t <= 1):
		x, y = 0, 0
		for i in range(0, n+1):
			b = factn / ((factoral(i)) * (factoral(n - i))) #binomial coefficient
			k = ((1 - t) ** (n - i)) * (t ** i) 			#powers
			x += b * k * xval[i] 							#parametric application
			y += b * k * yval[i] 							#to x and y
		turtle.goto(x, y)
		t += step
