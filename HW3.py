# Задание №2 Вычислить сумму цифр случайного трёхзначного числа
# from random import randint
# a = randint(100, 999)
# print(a)
# b = str(a)
# a1 = int(b[0])
# a2 = int(b[1])
# a3 = int(b[2])
# s = a1+a2+a3
# print(s)


# Вводиться строка. Удалить из неё все пробелы. После этого определить, является ли она палиндромом(перевертышем),
# т.е. одинаково пишется, как сначала, так и с конца

# a = input('Введи строку: ')
# b = a.replace(' ', '')
# print('Строка без пробелов: ', b)
# c = b[::-1]
# print('Перевернутая строка', c)
# if c == b:
#     print('Строка палиндром ')
# else:
#     print('Строка не палиндром')



# Задача №1
# 1.Дана строка.
# 2.Сначала выведите третий символ этой строки.
# 3. Во второй строке выведите предпоследний символ этой строки.
# 4. В третьей строке выведите первые пять символов этой строки.
# 5.В четвертой строке выведите всю строку, кроме последних двух символов.
# 6. В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0,
# поэтому символы выводятся начиная с первого).
# 7. В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# 8. В седьмой строке выведите все символы в обратном порядке.
# 9. В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
# 10. В девятой строке выведите длину данной строки.


str1 = 'Perehrest Anton Aleksandrovich'
print('1. Третий символ строки: ', str1[2])
print('2.Предпоследний символ: ', str1[-2])
print('3.Первые 5 символов', str1[:5])
print('4. Вся строка кроме последних двух:', str1[0:-2])
print('5. Символы с четными индексами:', str1[::2])
print('6. Символы с нечетными индексами:', str1[1::2])
print('7. В обатном порядке:', str1[::-1])
print('8. Все символы строки через один в обратном порядке, начиная с последнего:', str1[::-2])
print('Длинна строки', len(str1))