from doctest import run_docstring_examples

def run_doctests(func):
    """
    Roda os exemplos de teste definidos na docstring de uma função.

    Args:
        func (callable): Função a ser testada.
    """
    run_docstring_examples(func, globals(), func.__name__)
def uses_any(word, letters):
        """
           Verifica se uma palavra utiliza qualquer letra da string fornecida.

           Args:
               word (str): Palavra a ser analisada.
               letters (str): String contendo as letras a verificar.

           Returns:
               bool: True se a palavra usar qualquer letra da string, False caso contrário.
           """
        for letter in word.lower():
            if letter in letters.lower():
                return True
        return False

def uses_all(word, required):
    """checa se utiliza todas as letras requiridas

    """
    for letter in required.lower():
        if letter not in word.lower():
            return False
    return True

def uses_only(word, avaible):
        """Recebe uma palavra e uma string de letras e retorna True se a palavra contiver
        apenas letras presentes na string
        """
        for letter in word.lower():
            if letter not in avaible.lower():
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
