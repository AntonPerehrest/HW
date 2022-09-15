# Есть файл text.txt. Вывести слово, имеющее минимальную длину. Обработать исключения.
try:
    with open('text.txt', 'r', encoding='utf-8') as f:
        s = f.read()
except FileNotFoundError:
    print('Невозможно открыть')
print(s)
s = s.replace('\n',' ')
print(s)
import string
for i in s:
    if i in string.punctuation:
        s = s.replace(i,' ')
print(s)
s = s.split()
print(s)
print('min -', min(s, key=len), '\nmax -',max(s, key=len))





