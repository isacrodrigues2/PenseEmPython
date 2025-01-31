import re


text = 'I am Dracula; and i bid you welcome, Mr.Harker to my house'
pattern = 'Dracula'
result = re.search(pattern, text)
print(f'{result}/n' )
print('*=' * 8)
#Se o padrão for encontrado no texto, a função search retorna um objeto match
#que contém os resultados da busca
#Entre outras informações, o objeto tem uma variável chamda string, que contém o texto que foi pesquisado


print('*=' * 8)
#Também fornece uma função chamada group, que retorna a a parte do texto que correspondeu ao padrão
print(result.group())
print('*=' * 8)
#ALém disso, oferece uma função chamada span que retorna o índice no texto no qual o oadrão começa e termina
print(result.span())
print('*=' * 8)
#Se o padrão não for encontrado no texto, o valor retornado pela função search será none
result = re.search('count', text)
print(result)
print('*=' * 8)