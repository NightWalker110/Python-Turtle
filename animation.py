import turtle
from random import choice

pencil = turtle.Turtle()
pencil.speed(100)
COLOURS = ['yellow' , 'black' , 'green' , 'blue']

for j in range(180):
    c = choice(COLOURS)
    pencil.pencolor(c)
    pencil.forward(100)
    pencil.right(30)
    pencil.forward(20)
    pencil.left(60)
    pencil.forward(50)
    pencil.right(30)
    pencil.penup()
    pencil.setposition(0,0)
    pencil.pendown()
    pencil.right(2)
turtle.done()    
