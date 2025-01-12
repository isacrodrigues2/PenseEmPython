
import turtle
def parallelogram(length1,  length2, angle):
    for i in range(2):
        forward(length1)
        left(angle)
        forward(length2)
        left(180-angle)

def rectangle (length1, length2):
    parallelogram(length1,length2,angle)
    for i in range (2):
        turtle.forward(length1)
        turtle.left(90)
        turtle.forward(length2)
        turtle.left(90)



rectangle(80, 40,)