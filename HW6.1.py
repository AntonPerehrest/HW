#Задание №1 Дан произвольный список. Представьте его в обратном порядке.
# a = ['кот','слон','змея',1,2,3,4]
# a.reverse()
# print(a)
# print(a[::-1])  # вариант 2

#Задание №2  Дан список некоторых целых чисел, найдите значение 20 в нем и, если оно присутствует, замените его на 200.
# Обновите список только при первом вхождении числа 20.

# a = [1,4,6,9,44,11,20,4,1,20]
# n = a.index(20)
# a.remove(20)
# a.insert(n, 200)
# print(a)
#
# b = a.index(20) # Вариант 2
# a[b] = 200
# print(a)

# #  Задача 3 Найти совпадающие элементы двух списков.
# a = [5,[1,2],2,'r',4,'ee']
# b = [4,'we','ee',3,[1,2]]
# Эти значения записать в новый список


# a = [5,[1,2],2,'r',4,'ee']
# b = [4,'we','ee',3,[1,2]]
# r = []
# for i in a:
#     for j in b:
#         if i == j:
#             r.append(i)
# print(r)



#  Задача 3  Даны 2 списка:
# a = [4,6,'pу',78]
# b = [44,'hello’,56,'exept’,3]
# Выполнить следующие операции:
# Сложить два списка
# Добавьте элемент 6 на 3 позицию в 2м списке.
# Удалите все текстовые переменные
# 4.  Посчитайте количество элементов списка

# a = [4,6,'pу',78]
# b = [44,'hello',56,'exept',3]
# #1
# print(a+b)
# #2
# b.insert(2,6)
# print(b)
# #3
# for i in a:
#     if type(i) is str:
#         a.remove(i)
#         a.sort()
# print(a)
# #4
# print(len(b))

# Задача №1
# Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность. Если число чётное, то посчитать сумму его цифр.
# Если нечётное, то заменить  его на 1 в списке.
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.
#
#
lis=[15,48,'hello',6,19,'world']
gl = 0
sgl = 0
for i in lis:
    if type(i) is int:
        if i % 2 == 0:
            a = i//10
            b = i % 10
            print('Сумма цифр',i,'=',a+b)
            print('Сумма всех цифр',i,'=',int((1+i)*i/2))
        elif i % 2 != 0:
            c = lis.index(i)
            lis[c] = 1
    elif type(i) is str:
        glas = 'eyuioa'
        for j in i:
            if j in glas:
                gl += 1
            else:
                sgl += 1
        print(i,'гласных',gl)
        print(i,'согласных',sgl)
        gl = 0
        sgl = 0
print(lis)
print(lis)
print(lis)












