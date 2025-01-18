import math

'''
    Calcula o valor da hipotenusa de um triângulo retângulo
    b = tamanho do primeiro cateto
    c = tamanho do segundo cateto
    return a = retorna o comprimento da hipotenusa 
'''
def hipot(b,c):
    a = math.sqrt( (b ** 2) + (c ** 2))
    return a

#informa o valor dos catetos
cateto_1 = float(input('Informe o valor do primeiro cateto: '))
cateto_2 =float(input('Informe o valor do segundo cateto: '))

#calcula hipotenusa
hipotenusa = hipot(cateto_1,cateto_2)

# retorna o resultado
print(f'A hipotenusa é {hipotenusa}')
