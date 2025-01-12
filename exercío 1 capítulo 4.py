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


def parallelogram(length1,  length2, angle):
    for i in range(2):
        turtle.forward(length1)
        turtle.left(angle)
        turtle.forward(length2)
        turtle.left(180-angle)


def rhombus(length1,length2):
    parallelogram(length1,length2,90)

def rectangle (length1, length2, ):
    parallelogram(length1,length2,90)

jump(-120)

rectangle(80, 40)
jump(100)
rhombus(50,60)
jump(80)
parallelogram(80,40,60)