from pprint import pprint
import math
from click import prompt
from prompt_toolkit.input import Input
from xlrd.formula import listsep
from time import sleep

"""def calculo_hora ():
    start = 11
    duration = 3
    end = (start + duration) %12
    print(f'{end}')
calculo_hora()"""

"""def countdown (n):
    if n <= 0:
        print('Blastoff!!')
    else:
        print(n)
        countdown(n-1)
countdown(int(input("escolha um número:")))"""


'''def print_n_times(string, n):
    if n > 0:
        print(string)
        print_n_times(string, n-1)


print_n_times("SPAM", 4)'''

'''prompt = "What... is the airspeed velocity of a unladen swallow\n"
speed = input(prompt)
int(speed)'''

'''numerator = 9
denominator = 10
ratio = numerator/denominator
decibels = 10 * math.log10(ratio)

print(decibels)
'''
'''dict = {}
lista = [1,2,3,4,5,6,7,8,9,10,13]
def calcula_primo(n):
    for i in range(n):
        if n % lista[n] == 0:
            print(f"{n} é primo")

calcula_primo(int(input('Digite até qual valor deseja calcular o número primo')))'''

'''def countdown_by_two(n):
    if n==0:
        print('Blastoff!!')
    else:
        sleep(1)
        print(n)
        countdown_by_two(n-2)

countdown_by_two(80)
'''

