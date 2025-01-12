from turtle import forward, left

'''def rhombus(length, angle):
    for i in range(2):
        forward(length)
        left(angle)
        forward(length)
        left(180-angle)'''

#rhombus(50 , 60)

def parallelogram(length1,  length2, angle):
    for i in range(2):
        forward(length1)
        left(angle)
        forward(length2)
        left(180-angle)


def rhombus(length1,length2, angle):
    parallelogram(length1,length2,angle)

parallelogram(80,40,60)