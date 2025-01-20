

count = 0
total = 0
def has_e(word):
    return 'e' in word.lower()

for line in open('words.txt'):
    word = line.strip()
    total += 1
    if has_e(word):
        count += 1


# Exibindo o resultado final
print(f"Total de palavras: {total}")
print(f"Palavras com 'E' ou 'e': {count}")