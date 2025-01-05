def print_twice (string):
    for i in range (2):
        print(string)


def cat_twice (part1, part2):
    cat = part1 + part2
    print_twice(cat)
#vejamos um exemplo de uso dessa função
line1= 'Sorvete é'
line2= ' bão'
cat_twice(line1, line2)
#quando cat_twice é executada, ela cria uma variável local chamada cat, que é destruída assim que a função termina.
# se tentarmos exibil-a, recebemos um name erros
print(cat)