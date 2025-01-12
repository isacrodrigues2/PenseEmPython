import math

import turtle

def jump(length):
    turtle.penup()
    turtle.forward(length)
    turtle.pendown()

def triangle(radius, angle):
    y = radius * math.sin(angle * math.pi / 180)
    turtle.right(angle)
    turtle.forward(radius)
    turtle.left(90 + angle)
    turtle.forward(2 * y)
    turtle.left(90 + angle)
    turtle.forward(radius)
    turtle.left(180 - angle)

def draw_pie (n , radius):
    angle = 360 / n
    for i in range (n):
        triangle(radius, angle/2)
        turtle.left(angle)

# Criando o desenho com Turtle
screen = turtle.Screen()
jump(-80)
size = 50
draw_pie(5, size)
jump(2*size)
draw_pie(6, size)
jump(2*size)
draw_pie(7, size)

# Salvando como PostScript
ps_file = "drawing.ps"
screen.getcanvas().postscript(file=ps_file)
