
import turtle

def rectangle (largura, altura):
    turtle.forward(largura)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(largura)
    turtle.left(90)
    turtle.forward(altura)


rectangle(80, 40)