"""this program is to generate two diamonds using turtle graphics"""

import turtle

# predefine the diamond side length
SIDE_LENGTH = 100
# predefine the fill color
FILL_COLOR = "blue"

# setup the turtle window
turtle.setup(500, 600)

# setup the turtle
turtle.hideturtle()
turtle.fillcolor(FILL_COLOR)

# draw the left-side diamond first using the predefined SIDE_LENGTH
turtle.begin_fill()
turtle.right(45)
for i in range(4):
    turtle.forward(SIDE_LENGTH)
    turtle.right(90)
turtle.left(45)
turtle.end_fill()

# draw the right-side diamond next
turtle.penup()
turtle.forward(SIDE_LENGTH * 2)
turtle.pendown()

turtle.begin_fill()
turtle.right(45)
for i in range(4):
    turtle.forward(SIDE_LENGTH)
    turtle.right(90)
turtle.left(45)
turtle.end_fill()

turtle.done()
