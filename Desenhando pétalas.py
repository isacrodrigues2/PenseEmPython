from math import pi
from jupyturtle import forward, left, penup, pendown
import turtle

# Criando uma tela e uma tartaruga
screen = turtle.Screen()
t = turtle.Turtle()

def jump(length):
    t.penup()
    t.forward(length)
    t.pendown()

def polyline(n, length, angle):
    for i in range(n):
        t.forward(length)
        t.left(angle)

def arc(radius, angle):
    arc_length = 2 * pi * radius * angle / 360
    n = 30
    length = arc_length / n
    step_angle = angle / n
    polyline(n, length, step_angle)

def petal (radius, angle):
    for i in range (2):
        arc(radius , angle)
        t.left(180-angle)

def flower (n, radius, angle):
    for i in range (n):
        petal (radius, angle)
        t.left(360 / n)


jump(-60)
n = 7
radius = 60
angle = 60
flower(n, radius, angle)

jump(120)
n = 9
radius = 40
angle = 85
flower(n, radius, angle)

turtle.done()

