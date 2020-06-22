from turtle import Turtle
from random import randint

laura = Turtle()
laura.color('red')
laura.shape('turtle')
laura.penup()
laura.goto(-160,100)
laura.pendown()

for movemenent in range(100):
  laura.forward(randint(1,5))
