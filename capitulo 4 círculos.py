import turtle
from turtle import *
import math
from jupyturtle import make_turtle
'''
def polygon(n, length):
    angle = 360 / n
    for i in range(n):
        forward(length)
        left(angle)
    
polygon(7,89)


def circle(radius):
    circumference = 2 * math.pi * radius
    n = 30
    length = circumference/n
    polygon(n, length)
    make_turtle()
    circle(30)
'''
def polyline(n, length, angle):
    for i in range(n):
        forward(length)
        left(angle)



def polygon (n,length):
    angle = 360 / n
    polyline(n, length, angle)

def arc(radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360
    n = 30
    length = arc_length/ n
    step_angle = angle / n
    polyline(n , length, step_angle)

def circle(radius):
    arc(radius, 360)

make_turtle(delay=0)
polygon (20,9)
arc(70,70)
circle(10)