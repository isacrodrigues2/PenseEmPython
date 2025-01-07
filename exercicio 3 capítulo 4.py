from turtle import forward, left

def rhombus(length, angle):
    for i in range(2):
        forward(length)
        left(angle)
        forward(length)
        left(180-angle)

rhombus(50 , 60)