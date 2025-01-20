from doctest import run_docstring_examples


def run_doctests(func):
    """
    Roda os exemplos de teste definidos na docstring de uma função.

    Args:
        func (callable): Função a ser testada.
    """
    run_docstring_examples(func, globals(), func.__name__)


def uses_all(word, required):
    """checa se utiliza todas as letras requiridas

    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('ratatat', 'rat')
    True
    >>> uses_all('apple', 'api')
    False
    """
    for letter in required.lower():
        if letter not in word.lower():
            return False
    return True
'''print(uses_all('banana', 'ban'))

print(uses_all('ratatat', 'rat'))

print(uses_all('apple', 'apl'))'''



run_doctests(uses_all)