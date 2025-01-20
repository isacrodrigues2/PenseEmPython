from doctest import run_docstring_examples


def run_doctests(func):
    """
    Roda os exemplos de teste definidos na docstring de uma função.

    Args:
        func (callable): Função a ser testada.
    """
    run_docstring_examples(func, globals(), func.__name__)



def uses_none(word,letters):
     """
    Verifica se uma palavra evita as letras proibidas.

    Args:
        word (str): Palavra a ser analisada.
        letters (str): String contendo as letras proibidas.

    Returns:
        bool: True se a palavra evitar todas as letras proibidas, False caso contrário.

    Exemplos:
        >>> uses_none('banana', 'xyz')
        True
        >>> uses_none('apple', 'efg')
        False
    """
     for letter in letters:
         if letter in word:  # Se qualquer letra proibida estiver na palavra
             return False
     return True  # Retorna True apenas se nenhuma letra proibida estiver na palavra


# Testando a função com doctest
run_doctests(uses_none)
print(uses_none('banana', 'xyz'))

print(uses_none('apple', 'efg'))
