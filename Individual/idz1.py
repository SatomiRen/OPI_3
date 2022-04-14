import re
f = open('../Examples/text.txt', encoding='UTF')

while True:
    line = f.readline()
    if len(line) == 0:  # Нулевая длина обозначает конец файла
        break
    if not re.findall(r'\d{2}', line):
        print(line)

f.close()  # закрываем файл
