import turtle
import math
from drawing.animal import *

# Get user input
drawingPrompt = input("Enter prompt: ")

print(drawingPrompt)

turtle.penup()
turtle.pensize(5)
turtle.goto(-25, 25)
turtle.pendown()

cat_basic()

turtle.exitonclick()