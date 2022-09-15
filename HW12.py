# N = 2
# M = 3
# # A =[]
# # for i in range(N):
# #     A.append([0]*M)
# # print(A)
#
# A = [[0]*M for i in range(N)]
# print(A)


# a = [[1,2,3,4],[5,6],[7,8,9]]
# for i in range(len(a)):       # len(a) = 0,1,2
#     for j in range(len(a[i])):   #len(a[0]) = 0,1,2,3
#         print(a[i][j], end=' ')
#     print()

# N = 3
# M = 2
# A = [[0]*M for i in range(N)]
# print(A)
# for i in range(N):
#     for j in range(M):
#         A[i][j] = 1
#         print(A[i][j], end=' ')
#     print()

# import random
# N = int(input('Столбцы: '))
# M = int(input('Строки: '))
# A = [[0]*M for i in range(N)]
#
# for i in range(N):
#     for j in range(M):
#         A[i][j] = random.randint(1, 100)
#
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         print(A[i][j], end=' ')
#     print()

# a = {1:12,2:213,3:121}
# try:
#     value = a[4]
# except KeyError:
#     print('no key')

# Задача №1
# Матрица 5 х 5. Найти строку с максимальной суммой элементов и вывести её номер.
# from random import randint
# N = 5
# M = 5
# A = [[0]*M for i in range(N)]
#
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         A[i][j] = randint(1,100)
#         print(A[i][j], end=' ')
#     print()
#
# b =[]
# for k in A:
#     b.append(sum(k))
# print('Номер строки',(b.index(max(b))+1),'-', max(b))

#
# Задача №2
#
# Ввод с клавиатуры. Если строка введённая с клавиатуры – это числа, то поделить первое на второе.
# Обработать ошибку деления на ноль. Если второе число 0, то программа запрашивает ввод чисел заново.
# Также если были введены буквы, то обработать исключение.

#
# while True:
#     try:
#         a = int(input('Первое:'))
#         b = int(input('Второе:'))
#         print('Деление:', a/b)
#         break
#     except ValueError:
#         print('Введенное значение некорректно')
#     except ZeroDivisionError:
#         print('Попытка деления на ноль')
# print('конец)')

# Задача №3
# Матрица N x M, можно задать статически. Элементы заполняются случайными числами.
# Вводить с клавиатуры число и если оно есть в матрице, то вывести индекс строки и колонки в которой оно находится.

from random import randint
N = 5
M = 4
A = [[0]*M for i in range(N)]

for i in range(len(A)):
    for j in range(len(A[i])):
        A[i][j] = randint(1,100)
        print(A[i][j], end=' ')
    print()
a = int(input('Введи число: '))
for i in range(N):
    for j in range(M):
        if a == A[i][j]:
            print(' строка =', i+1,'\n'
                  ' колонка  =', j+1,'\n' 'позиция в строке =',
                  A[i].index(a)+1)