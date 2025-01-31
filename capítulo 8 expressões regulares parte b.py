import re

'''
aqui está uma função que itera sobre as linhas do livro até encontrar uma que corresponda
,ao padrão fornecido, e retorna o objeto MATCH:
'''
def find_first(pattern):
    for line in open('pg345_cleaned.txt'):
        result = re.search(pattern,line)
        if result != None:
            return result
'''
podemos utilizar um padrão como esse para verificiar quantas vezes um personagem é mencionadopor qualquer um dos nomes
A seguir apresentamos uma funçãoque percorre o livro e conta quantas linhas correspondem ao padrão fornecido
'''
def count_matches(pattern):
    count = 0
    for line in open('pg345_cleaned.txt'):
        result = re.search(pattern, line)
        if result != None:
            count += 1
    return count
print(count_matches('Mina|murray'))

#Para achar uma linha com uma palavra no começo da frase
#result = find_first('^Dracula')

#para achar uma linha com uma palavra no final da frase
#result = find_first('Harker$')

"""nesse padrão os parenteses delimitam a parte do padrão
à qual a barra vertical se aplica. Dessa forma, esse padrão corresponde, 
a uma sequeência que começa com 'cent' e termina com 'er' ou 're'

pattern = 'cent(re|er)'
result = find_first(pattern)
print(result.string)
"""
'''
O padrão a seguir utiliza o caractere especial '?', que indica que o caractere anterior é opcional
'''
pattern = 'colou?r'
result = find_first(pattern)
line = result.string
print(line)

'''
o primeiro argumento é o padrão que queremos localizar e substituir, o segundo é oque queremos
 colocar no lugar, e o terceiro é a string que queremos buscar.
'''
linha = re.sub(pattern,'color', line)
print(f'{linha}')

