'''from time import time

seconds_per_day = 24 * 60 * 60
now = time()
days = now // seconds_per_day
remainder = now % seconds_per_day
hours = remainder // 3600
remainder = remainder % 3600
minutes = remainder // 60
seconds = minutes % 60
print(f'{days} dias, {hours} horas, {minutes} minutos e {seconds} segundos')
'''
def is_triangle(a,b,c):
    if a > (b + c):
        print('não é um triángulo')
    elif b > (a + c ):
        print('não é um triángulo')
    elif c > (a + b ):
        print('não é um triángulo')
    else:
        print('parabéns voce tem um triângulo')
is_triangle(20 , 5, 8)