

# Задача №1
# Написать функцию, которая определяет количество разрядов введенного целого числа.

# def kol_razrad(num):
#     razrad = 0
#     while True:
#         num = num / 10
#         razrad += 1
#         if num < 1:
#             break
#
#     return razrad
#
#
# num = int(input('Введите целое число: '))
# print('Количество разрядов числа:', kol_razrad(num))


# Задача №2
# В зависимости от выбора пользователя вычислить площадь круга, прямоугольника или треугольника.
# Для вычисления площади каждой фигуры должна быть написана отдельная функция

# import math
# def sqrt_circle(radius): return 3.14 * (radius ** 2)
#
#
# def sqrt_rect(side_1, side_2): return side_1 * side_2
#
#
# def sqrt_triangle(a, b, c):
#     p = (a + b + c) / 2
#     sqr = math.sqrt(p * (p - a) * (p - b)*(p - c))
#     return sqr
#
#
# square = int(input('1 - круг, 2 - прямоугольник, 3 - треугольник \nКакую площадь вычислить?: '))
# if square == 1:
#     radius = int(input('Радиус круга: '))
#     print(sqrt_circle(radius))
#
# if square == 2:
#     side_1 = int(input('Первая сторона: '))
#     side_2 = int(input('Вторая сторона: '))
#     print(sqrt_rect(side_1, side_2))
#
# if square == 3:
#     a, b, c = map(int, input('3 стороны (через пробел): ').split())
#     if a + c < b or a + b < c or c + b < a:
#         print('Нет такого треугольника')
#         a, b, c = map(int, input('3 стороны (через пробел): ').split())
#     print(sqrt_triangle(a, b, c))


# Задача №3
# Написать функцию, которая заполняет массив длинной 10 элементов, случайными числами в диапазоне,
# указанном пользователем с клавиатуры. Функция должна принимать два аргумента – начало диапазона и его конец,
# при этом ничего не возвращать.

# import random
#
# a = [0] * 10
# mn = int(input('Начало: '))
# mx = int(input('Конец: '))
#
# def func(mn, mx):
#     for i in range(10):
#         a[i] = random.randint(mn, mx)
#
# func(mn, mx)
# print(a)
# 50000 = 0d

# Задача №4
# Написать функцию и сделать так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды

# def time(sek): return print(sek // 86400,'d:',
#                             sek % 86400 // 3600,'h:',
#                             sek % 86400 % 3600 // 60,'m:',
#                             sek % 86400 % 3600 % 60,'s')
#
# time(324324)


# Задача №5
# Написать функцию, которая считает сколько гласных и согласных в строке. Строку вводить с клавиатуры.
# import string
# stroka = input('Введите вашу строку: ')
# def glas_soglas(stroka):
#     gl = 0
#     sgl = 0
#     for i in stroka:
#         if i in 'eyuioa':
#             gl += 1
#         elif i in string.punctuation or i == ' ':
#             sgl += 0
#         else:
#             sgl += 1
#     return f'glas - {gl}, sogl - {sgl}'
#
# print(glas_soglas(stroka))



# Задача №6
# Функцию которая при заданном целом числе n посчитает n + nn + nnn

# num = int(input('Число: '))
#
#
# def n_nn_nnn(num): return f'{num} + {int(str(num) * 2)} + {int(str(num) * 3)} = ' \
#                           f'{num + int(str(num) * 2) + int(str(num) * 3)}'
#
#
# print(n_nn_nnn(num))


# Задача №6
#Вычислить значения нижеприведенной функции в диапазоне значений x от -10 до 10 включительно с шагом, равным 1.
# y = 𝑥^2 при -5 <= x <= 5;
# y = 2*|x|-1 при x < -5;
# y = 2x при x > 5.
# Вычисление значения функции оформить в виде программной функции, которая принимает значение x,
# а возвращает полученное значение функции (y).

# import math
# import random
#
# def one(x): return f'y = {x**2}'
#
# def two(x): return f'y = {2 * math.fabs(x) - 1}'
#
# def three(x): return f'y = {2 * x}'
#
# x = random.randint(-10, 10)
# print('x = ', x)
# if x in range(-5,6):
#     print('Первое условие', '\n',one(x))
# elif x < -5:
#     print('Второе условие', '\n',two(x))
# elif x > 5:
#     print('Третье условие', '\n',three(x))


# Задача №7
# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.
