def repeat(word, n ):
   print(word * n)

spam = 'Spam '
def first_two_lines():
    repeat(spam,4)
    repeat(spam, 4)

def last_three_lines():
    repeat(spam, 2)
    print('(Lovely Spam. Wonderful spam)')
    repeat(spam, 2)
def print_verse():
    first_two_lines()
    last_three_lines()


for i in range(2):
    print("Verse", i)
    print_verse()
    print()

