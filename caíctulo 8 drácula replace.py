
writer = open('pg345_replaced.txt', 'w')

for line in open('pg345_cleaned.txt'):
        line = line.replace('Jonathan', 'Thomas')
        writer.write(line)
        print(line)