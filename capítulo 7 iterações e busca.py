def has_e(word):
    for letter in word:
        print(letter)
        if letter == 'E' or letter == 'e':
            return True

    return False
print(has_e('gadsby'))
print(has_e('fatel'))
