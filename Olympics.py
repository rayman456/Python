import turtle

#Get radius
radius = input('Enter a radius:')
while(radius.isdigit() is False):
	print("Invalid")
	radius = input('Enter a radius:')
radius = int(radius)

#Calculate points
black = (0, 0)
blue = (-(radius * 2.3), 0)
red = (radius * 2.3, 0)
yellow = (-(radius * 2.3)/2, -radius * 1.3)
green = ((radius * 2.3)/2, -radius * 1.3)

#Begin Drawing
turtle.pensize(5)
turtle.showturtle()

turtle.circle(radius)

turtle.color("blue")
turtle.up()
turtle.setpos(blue)
turtle.down()
turtle.circle(radius)

turtle.color("red")
turtle.up()
turtle.setpos(red)
turtle.down()
turtle.circle(radius)

turtle.color("yellow")
turtle.up()
turtle.setpos(yellow)
turtle.down()
turtle.circle(radius)

turtle.color("green")
turtle.up()
turtle.setpos(green)
turtle.down()
turtle.circle(radius)

turtle.done()
