


def factorial(n):
    if not isinstance(n,int):
        print('Fatoriais são definidos somente por números inteiros')
        return 0
    elif n < 0:
        print('Fatoriais não são definidos por números negativos')
        return 0
    elif n == 0:
        return 1
    return n * factorial(n - 1)
print(factorial(5))