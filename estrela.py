import turtle
from random import random, randint

# for i in range(4):
#     turtle.pensize(5)
#
#     turtle.forward(250)
#     turtle.left(90)
#     # turtle.forward(250)
#     # turtle.left(90)
#     # turtle.forward(250)
#     # turtle.left(90)
#     # turtle.forward(250)
#     # turtle.left(90)
turtle.pensize(5)
turtle.colormode(255)

for i in range(5000):
    turtle.color(randint(0, 150),
          randint(0, 150),
          randint(0, 150))
    turtle.forward(200)
    turtle.left(216)

turtle.Screen().exitonclick()