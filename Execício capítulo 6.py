
import math

def absolute_value(x):
    if x < 0:
        return -x
    if x >= 0:  # Inclui 0 de forma explícita
        return x


print(absolute_value(5))
print(absolute_value(-5))

def is_divisible(x,y):
    if x % y == 0:
        return True
    else:
        return False

is_divisible(6,2)



def calculate_distance(x1, y1, x2, y2):
    """
    Calcula a distância euclidiana entre dois pontos no plano cartesiano.

    :param x1: Coordenada x do primeiro ponto.
    :param y1: Coordenada y do primeiro ponto.
    :param x2: Coordenada x do segundo ponto.
    :param y2: Coordenada y do segundo ponto.
    :return: A distância entre os dois pontos.
    """
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


# Exemplo de uso
point1 = (1, 2)
point2 =(4, 6)
result = calculate_distance(*point1, *point2)
print(f"A distância entre os pontos {point1} e {point2} é {result:.2f}")