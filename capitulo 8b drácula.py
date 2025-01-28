

reader = open('pg345.txt', 'r', encoding='utf-8')
writer = open('pg345_cleaned.txt', 'w')

def is_special_line(line):
    return line.startswith('***')
for line in reader:
    if is_special_line(line):
        break
for line in reader:
    if is_special_line(line):
        break
    writer.write(line)
reader.close()
writer.close()

for line in open('pg345_cleaned.txt'):
    if len(line) > 0:
        print(line)
    if line.endswith('Stoker'):
        break