import turtle


def sierpinski(t, length, depth):
    """
    Desenha um Triângulo de Sierpinski com a tartaruga.

    :param t: Objeto Turtle para desenhar.
    :param length: Comprimento do lado inicial.
    :param depth: Profundidade da recursão.
    """
    if depth == 0:
        for _ in range(3):
            t.forward(length)
            t.left(120)
    else:
        sierpinski(t, length / 2, depth - 1)
        t.forward(length / 2)
        sierpinski(t, length / 2, depth - 1)
        t.backward(length / 2)
        t.left(60)
        t.forward(length / 2)
        t.right(60)
        sierpinski(t, length / 2, depth - 1)
        t.left(60)
        t.backward(length / 2)
        t.right(60)


# Configuração da tartaruga
#turtle = turtle()

# Posiciona a tartaruga no local inicial
turtle.penup()
turtle.goto(-100, 50)  # Ajusta a posição inicial
turtle.pendown()

# Desenha o Triângulo de Sierpinski
side_length = 200  # Tamanho do lado inicial
recursion_depth = 4  # Profundidade da recursão
sierpinski(turtle, side_length, recursion_depth)