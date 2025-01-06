"""escreva uma função chamada triangle que receba uma string e um número inteiro,
e desenhe um triãngulo com a altura especificada, composto de múltiplas cópias da string."""

def triangle(string, height):
    """
    Desenha um triângulo com a altura especificada, composto de múltiplas cópias da string.

    :param string: A string usada para formar o triângulo.
    :param height: A altura do triângulo (número de linhas).
    """

    for i in range(1, height + 1):
        print(string * i)


triangle("*", 4)