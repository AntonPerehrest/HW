# def a():
#     sum = 0
#     for i in range(10):
#         sum += i
#     print(sum)
# a()
import random


# def add(a,b):
#     return a + b
# print(add(a=1,b=2))
#
# c = add(a=3,b=4)
# print(c)


# def a(*args,**kwargs):
#     print(args)
#     print(kwargs)
# a(1,2,3,4,5, name = 'Anton', age = '24')

# def add(a,b):
#     def bdd(x):
#         return x * x * x
#     return bdd(a) + bdd(b)
# print(add(2,3))

#високоснвый год
# def add(year = int(input('year: '))):
#
#     if year % 4 == 0 and year % 100 !=0 or year % 400 ==0:
#         print('Високосный')
#     else:
#         print('Невисокосный')
# add()

#Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата. Сторону квадрата вводить с клавиатуры

# import math
# def square(a = int(input('side:'))):
#     return a*4, a*a, a*math.sqrt(2)
#
# print(square())

#Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
# Номер месяца вводить с клавиатуры.
# while True:
#     def sesaon(a = int(input('season: '))):
#
#         if a == 12 or a == 1 or a == 2:
#             print('winter')
#         elif a == 3 or a == 4 or a == 5:
#             print('spring')
#         elif a == 6 or a == 7 or a == 8:
#             print('summer')
#         elif a == 9 or a == 10 or a == 11:
#             print('summer')
#         else:
#             print('invalid value')
#     sesaon()

#Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе
# from random import randint
#
# def is_prime():
#     x = randint(0,1000)
#     print(x)
#     for i in range(2, (x//2)+1):
#
#         if x % i == 0:
#             a = 'false'
#         else:
#             a = 'True'
#     print(a)
#
#
# is_prime()

#Функция, вычисляющая среднее арифметическое элементов массива. Массив должен состоять из случайных чисел,
# длинной 10 элементов
# import random
# def sr_ar():
#     a = tuple([random.randint(0,100) for i in range(10)])
#     print(a)
#     print(sum(a))
#
# sr_ar()

# калькулятор

# def kalk():
#     while True:
#         a = int(input('Первое число: '))
#         b = int(input('Второе число: '))
#         c = input('Оператор: ')
#         if c == '*':
#             print(a, c, b, '=', a * b)
#         if c == '/':
#             try:
#                 print(a, c, b, '=', a / b)
#             except ZeroDivisionError:
#                 print('Деление на ноль')
#         if c == '+':
#             print(a, c, b, '=', a + b)
#         if c == '-':
#             print(a, c, b, '=', a - b)
#         if a == 0:
#             return print('конец')
#         break
#
#
# kalk()







# print('two numbers:')
# a = int(input())
# b = int(input())
# print('+','-','*','/','0-exit')
# print('operator:')
#
#
# def plus(a, b):
#     return a + b
#
#
# def minus(a, b):
#     return a - b
#
#
# def proizv(a, b):
#     return a * b
#
#
# def delen(a, b):
#     if b == 0:
#         return 'error'
#     else:
#         return a / b
#
# while True:
#     x = input()
#     if x == '0':
#         print('end')
#         break
#     else:
#         if x =='+':
#             print('result:', plus(a, b))
#         if x =='-':
#             print('result:', minus(a, b))
#         if x =='*':
#             print('result:', proizv(a, b))
#         if x =='/':
#             print('result:', delen(a, b))
#         print('operator:')