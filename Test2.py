# a = [5,[1,2],2,'r',4,'ee']
# b = [4,'we','ee',3,[1,2]]
# c = []
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)

#Даны 2 списка:
# a = [4,6,'pу',78]
# b = [44,'hello’,56,'exept’,3]
# Выполнить следующие операции:
# Сложить два списка
# Добавьте элемент 6 на 3 позицию в 2м списке.
# Удалите все текстовые переменные
# 4.  Посчитайте количество элементов списка
# a = [4,6,'pу',78]
# b = [44,'hello',56,'exept',3]
# print(a+b)
# b.insert(2,6)
# print(b)
# c = a + b
# print(c)
# for i in c:
#     if type(i) is str:
#         c.remove(i)
# print(c)
# print(len(c))

# Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность. Если число чётное, то посчитать сумму его цифр.
# Если нечётное, то заменить  его на 1 в списке.
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.
# list=[15,48,'hello',6,19,'world']
# gl = 0
# sgl = 0
# for i in list:
#     if type(i) is int:
#         if i % 2 == 0:
#             print(i//10 + i % 10)
#         else:
#             list[list.index(i)] = 1
#     elif type(i) is str:
#         for j in i:
#             if j in 'eyouai':
#                 gl += 1
#             else:
#                 sgl += 1
#         print(i,sgl,gl)
#         gl=0
#         sgl = 0

#Список из 7 цифр. Если четных цифр в нем больше чем нечетных, то найти сумму всех его цифр,
# если нечетных больше, то найти произведение 1 3 и 6 элемента.
# a = [1,7,4,2,3,8,3]
# ch = 0
# nch = 0
# for i in a:
#     if i % 2 == 0:
#         ch += 1
#     else:
#         nch += 1
# if ch > nch:
#     print('all',sum(a))
# else:
#     print(a[0]*a[2]*a[5])


from random import randint
# a = [randint(0,100) for i in range(10)]
# b = tuple(a)
# print(b)
# print(max(b), min(b))

a = tuple((randint(0,5) for i in range(10)))
b = tuple((randint(-5,0) for i in range(10)))
c = a + b
print(c, c.count(0))
