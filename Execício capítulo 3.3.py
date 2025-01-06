"""escreva uma função chamada retangle que receba uma string e um número inteiro,
e desenhe um retângulo com a altura e largura especificads, composto de múltiplas cópias da string."""

def retangle(string, height, widht):
    """
    Desenha um retâgulo com a altura e largura especificada, composto de múltiplas cópias da string.

    :param string: A string usada para formar o triângulo.
    :param height: A altura do triângulo (número de linhas).
    :param height: A largura do triângulo (número de letras).
    """

    for i in range(1, height + 1):
        print(string * widht)


retangle(input('Infome a palavra ou letra para compor o retangulo'), 4,5)