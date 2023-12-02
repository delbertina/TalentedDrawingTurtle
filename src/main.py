import turtle
import math
from drawing.animal import *

# Get user input
drawingPrompt = input("Enter prompt: ")

print(drawingPrompt)

startingX = 0 - ((turtle.window_width() / 2) - 25)

turtle.penup()
turtle.pensize(5)
turtle.goto(startingX, 25)
turtle.pendown()

cat_basic()
turtle.penup()
turtle.forward(50)
turtle.pendown()
fish_basic()
turtle.penup()
turtle.forward(50)
turtle.pendown()
bird_basic()
turtle.penup()
turtle.forward(50)
turtle.pendown()
snake_basic()


turtle.exitonclick()