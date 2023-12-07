import turtle
import math
from drawing.animal import *

def reset_for_next_drawing():
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()

# Get user input
drawingPrompt = input("Enter prompt: ")

print(drawingPrompt)

startingX = 0 - ((turtle.window_width() / 2) - 25)

turtle.penup()
turtle.pensize(5)
turtle.goto(startingX, 25)
turtle.pendown()

cat_basic()
reset_for_next_drawing()
fish_basic()
reset_for_next_drawing()
bird_basic()
reset_for_next_drawing()
snake_basic()
reset_for_next_drawing()
lion_adult_male()
reset_for_next_drawing()
penguin_basic()
reset_for_next_drawing()
rabbit_basic()
reset_for_next_drawing()
shark_basic()


turtle.exitonclick()