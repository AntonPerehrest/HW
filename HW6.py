# Задача 1. Перемножить все неч значения от 1 до 100

# a = 1
# b = 1
# for i in range(1,126):
#     if i % 2 == 0:
#         b = a
#         a *=i
#
#         print(b,'*',i,'= ',a)

# Задача 2. Записать в массив все числа от 1 до 500 кратные 5

# mas = []
# for i in range(1,501):
#     if i % 5 == 0:
#         mas.append(i)
# print(mas)

# a = [1,2,3,4,5,6,2,1,4,6,3,1,3,5,6,3,6]
# b = []
# for i in a:
#     if a.count(i) >= 2:
#         b.append(i)
# print(b)


#вывести отрицательные между числами
# a = int(input('one '))
# b = int(input('two '))
# while a > b:
#     b +=1
#     for i in range(b,a):
#         if i < 0:
#             print(i)
#     break
# else:
#     a +=1
#     for i in range(a,b):
#         if i < 0:
#             print(i)

# калькулятор

# a = int(input('one '))
# b = int(input('two '))
# c = input('оператор ')
#
# if c == '+':
#     print('сумма')
#     print(a,'+',b, '=',a+b)
# elif c == '-':
#     print('вычетание')
#     print(a,'-',b, '=',a-b)
# elif c == '*':
#     print('умножение')
#     print(a, '*', b, '=', a * b)
# elif c == '/':
#     if b != 0:
#         print('деление')
#         print(a, '/', b, '=', a / b)
#     else:
#         print('xyu')
#Способ №2
# a = int(input('one '))
# b = int(input('two '))
#
# while True:
#     c = input('оператор ')
#     if a == 0:
#         break
#     elif c == '+':
#         print('сумма')
#         print(a,'+',b, '=',a+b)
#     elif c == '-':
#         print('вычетание')
#         print(a,'-',b, '=',a-b)
#     elif c == '*':
#         print('умножение')
#         print(a, '*', b, '=', a * b)
#     elif c == '/':
#         if b != 0:
#             print('деление')
#             print(a, '/', b, '=', a / b)
#         else:
#             print('xyu')


# задача. массив из 7 цифр. Если четных цифр в нем больше чем нечетных, то найти сумму всех его цифр
# если нечетных больше, то найти произведение 1, 3 и 6 элемента

# a = [1,3,5,6,7,3,6,4,2,6,7,3,10]
# nech=[]
# chet=[]
# b = 0
# for i in a:
#     if i % 2 != 0:
#         nech.append(i)
#     else:
#         chet.append(i)
# if len(nech) > len(chet):
#     print(a[0],'*',a[2],'*',a[5],'=', a[0]*a[2]*a[5])
# elif len(nech) == len(chet):
#     print('Четных и нечетных одинаковое количество')
# else:
#     for j in chet:
#         b += j
#     print('Сумма четных = ', b)


# Казино. Компьютер генерирует числа от 1 до 10 и от 1 до 2-х Соответственно. Цифры от одного до 10 отвечают за номера,
# а от 1 до 2 за цвета(1-красный,2 черный).
# Пользователю дается 5 попыток угадать номер и цвет(Прим. введения с клавиатуры: 3 красный).
# В случае неудачи вывести на экран правильную комбинацию.
#
# from random import randint
#
# number = randint(1, 10)
# color = randint(1, 2)
# if color == 1:
#     color = 'красный'
# else:
#     color = 'черный'
# print(number, color)
# n = 5
# print('Угадай комбинацию')
# while n != 0:
#     print('У вас осталось',n,'попыток')
#     my_num, my_col = input('Введи: ').split()
#     my_num = int(my_num)
#     if my_num == number and my_col == color:
#         print('Поздравляю! Верная комбинация')
#         break
#     else:
#         n -= 1
#         print('Не угадали. Верная комбинация:', number, color)
#     if n == 0:
#         print('Попытки закончились')


# Казино. Компьютер генерирует числа от 1 до 10 и от 1 до 2-х Соответственно. Цифры от одного до 10 отвечают за номера,
# а от 1 до 2 за цвета(1-красный,2 черный).
# Пользователю дается 5 попыток угадать номер и цвет(Прим. введения с клавиатуры: 3 красный).
# В случае неудачи вывести на экран правильную комбинацию.

4a = 5
from random import randint
number = randint(1,10)
color = randint(1,2)
# print(number, color)
n = 5
while n > 0:
    print('У вас',n, 'попыток')
    a = int(input('Введите число: '))
    b = int(input('Введите цвет (1 - красный, 2 - черный): '))
    if a > number:
        print('Ваше число больше')
        if b == color:
            print('но вы угадали цвет')
        else:
            print('Вы не угадали цвет')
    elif a < number:
        print('Ваше число меньше')
        if b == color:
            print('но вы угадали цвет')
        else:
            print('Вы не угадали цвет')
    elif a == number:
        print('Вы угадали число')
        if b != color:
            print('Но вы не угадали цвет')
        else:
            print('Вы угадали цвет')
            print('Поздравляю!')
            break
    n -=1
    if n == 0:
        print('Попробуйте снова')
