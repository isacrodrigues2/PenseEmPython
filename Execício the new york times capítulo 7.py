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
     apenas letras presentes na string"""

    for letter in word.lower():
        if letter not in avaible.lower():
            return False
    return True

def uses_all(word, required):
    """Checks whether a word uses all required letters.
    """
    for letter in required.lower():
        if letter not in word.lower():
            return False
    return True

def check_word(word, available, required):
    """checa se a palavra é aceitavel.

    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """
    if len(word) < 4:
        return False
    if not uses_all(word,required):
        return False

    return uses_only(word,available)

run_doctests(check_word)