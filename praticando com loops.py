def repeat(word, n ):
   print(word * n)

spam = 'Spam '
def first_two_lines():
    repeat(spam,4)
    repeat(spam, 4)

def last_three_lines():
    repeat(spam, 2)
    print('(Lovely Spam. Wonderful spam!)')
    repeat(spam, 2)
def print_verse():
    first_two_lines()
    last_three_lines()

for i in range(2):
    print("Verse", i)
    print_verse()
    print()

def print_n_verses(n):
    for i in range(n):
        print_verse()
        print()

print_n_verses(int(input('Informe q quantidade de vezes que quer repetir: ')))