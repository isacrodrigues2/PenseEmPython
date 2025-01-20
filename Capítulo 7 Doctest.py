from doctest import run_docstring_examples


def run_doctests(func):
    run_docstring_examples(func, globals(), func.__name__)

def uses_any(word,letters):
    """
       Verifica se uma palavra utiliza qualquer letra da string fornecida.

       Args:
           word (str): Palavra a ser analisada.
           letters (str): String contendo as letras a verificar.

       Returns:
           bool: True se a palavra usar qualquer letra da string, False caso contrário.

       Exemplos:
           >>> print(uses_any('banana', 'aeiou'))
           True
           >>> print(uses_any('sky', 'aeiou'))
           False
       """
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False



def uses_any_incorrect(word, letters):

    """
       Verifica se uma palavra utiliza qualquer letra da string fornecida.

       Args:
           word (str): Palavra a ser analisada.
           letters (str): String contendo as letras a verificar.

       Returns:
           bool: True se a palavra usar qualquer letra da string, False caso contrário.

       Exemplos:
           >>> print(uses_any_incorrect('banana', 'aeiou'))
           True
           >>> print(uses_any_incorrect('sky', 'aeiou'))
           False
      """

    for letter in word.lower():
        if letter in letters.lower():
            return True
        else:
            return False #incorect


run_doctests(uses_any)