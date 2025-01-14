from turtle import forward, left, right, back

from jupyturtle import make_turtle


def koch(x):
    if x < 5:
        forward(x)
    else:
        koch(x/3)
        left(60)
        koch(x / 3)
        right(120)
        koch(x / 3)
        left(60)
        koch(x / 3)


make_turtle(delay=0.2)
koch(120)