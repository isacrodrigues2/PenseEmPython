from turtle import *

def polygon (n, length):
    angle = 360 / n
    for i in range (n):
        forward(length)
        left(angle)

polygon(7,30)
