from doctest import run_docstring_examples


def run_doctests(func):
    """
    Roda os exemplos de teste definidos na docstring de uma função.

    Args:
        func (callable): Função a ser testada.
    """
    run_docstring_examples(func, globals(), func.__name__)

def uses_only(word,avaible):
    """Recebe uma palavra e uma string de letras e retorna True se a palavra contiver
     apenas letras presentes na string

    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('ratatat', 'rate')
    True
    >>> uses_only('apple', 'apl')
    False
    """
    for letter in word.lower():
        if letter not in avaible.lower():
            return False
    return True

run_doctests(uses_only)