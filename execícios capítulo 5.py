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

'''exemplo de recursividade
def recurse(n,s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse (3,0)'''