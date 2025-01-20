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

    """
    for letter in required.lower():
        if letter not in word.lower():
            return False
    return True

def word_score(word, available):
    """Calcula a pontuação de uma palavra válida
    >>> word_score('card','ACDLORT')
    1
    >>> word_score('color','ACDLORT')
    5
    >>> word_score('Cartload','ACDLORT')
    15
    """
    n= len(word)
    if n == 4:
        return 1
    if uses_all(word, available):
        return n + 7
    return n

print(word_score('card', 'ACDLORT'))
print(word_score('color', 'ACDLORT'))
print(word_score('Cartload', 'ACDLORT'))
