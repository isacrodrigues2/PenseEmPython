import turtle

def jump(length):
    turtle.penup()
    turtle.forward(length)
    turtle.pendown()

turtle.delay(200)
turtle.forward(100)
jump(10)
turtle.forward(100)
turtle.left(90)
jump(10)
turtle.forward(100)
