# Размерность матрицы вводится с клавиатуры, заполнить матрицу случайными числами от 10 до 50.
# Найти наибольшую сумму элементов в столбцах матрицы. Вывести индекс столбца с максимальной суммой элементов на экран

from random import randint
N = int(input('строки: '))
M = int(input('столбцы: '))
A = [[0]*M for i in range(N)]

for i in range(len(A)):
    for j in range(len(A[i])):
        A[i][j] = randint(10,50)
        print(A[i][j], end=' ')
    print()
z = []
for i in range(len(A[0])):
    stolb = 0
    for j in range(len(A)):
        stolb += A[j][i]
    z.append(stolb)
print(z)
print('Максимальная сумма у столбца №', z.index(max(z))+1,'-',max(z))

