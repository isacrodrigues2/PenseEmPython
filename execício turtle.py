from turtle import forward, left, right, back

def draw (length):
    angle = 60
    factor = 0.8

    if length > 5:
        forward(length)
        left(angle)
        draw (factor * length)
        right (2 * angle)
        draw(factor * length)
        left(angle)
        back(length)
draw(100)