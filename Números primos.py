from pandas.io.formats.format import return_docstring


def is_prime(n):
    """
    Verifica se um número é primo.
    Retorna True se o número for primo, caso contrário, False.
    """
    if n <= 1:
        return False
    for i in (range(2, int(n**0.5) + 1)):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    """
    Retorna uma lista de números primos em um intervalo [start, end].
    """
    primes = []
    for n in range(start, end + 1):
        if is_prime(n):  # Usa a função is_prime definida acima
            primes.append(n)
    return primes

# Exemplo de uso
print(primes_in_range(10, 50))