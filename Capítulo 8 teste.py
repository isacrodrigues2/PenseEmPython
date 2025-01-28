def compare_word(word):
    if word < 'banana':
        print(word, 'comes before banana')
    elif word > 'banana':
        print(word, 'comes after banana')
    else:
        print('All right, banana')

compare_word(input('Digite sua palavra: ').strip().lower())