

reader = open('pg345.txt', 'r', encoding='utf-8')

def is_special_line(line):
    return line.startswith('***')
for line in reader:
    if is_special_line(line):
        print(line.strip())
