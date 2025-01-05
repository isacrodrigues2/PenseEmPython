#Definição de uma função que requer argumento
def print_twice(string):
    print(string)
    print(f'{string} \n')
print_twice('Dennis moore')

#Executar essa função tem o mesmo efeito que atribuir o argumentoao parâmetro, e em seguida,
#executar o corpo da função, como no exemplo a seguir
string = ('Dennis Moore, '
          '')
print(string)
print(f'{string} \n')

#também é possível utilizar uma variável como argumento
line = 'Dennis Moore'
print_twice(line)
