'''escreva uma função booleana is_between(x,y,z) que retorna True se X<Y<Z ou se x > y > z; caso contrário, retorne Falso'''


def is_between(x,y,z):
    if x < y < z:
        return True
    elif x > y > z:
        return True
    else:
        return False


print(is_between(1,2,3))
print(is_between(3,2,1))
print(is_between(2,3,1))
print(is_between(2,2,2))


