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