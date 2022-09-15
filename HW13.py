# try:
#     file1 = open('1.txt', 'w')
#     try:
#         file1.write('line11\n')
#     finally:
#         file1.close()
#         file1 = open('1.txt', 'r')
#         print(file1.read())
# except FileNotFoundError:
#     print('ece')



# import pickle
#
# books = [('Евгений Онегин', 'Пушкин А.С.',200),
#          ('Муму','Тургеньев И.С.', 250),
#          ('Мастер и Маргарита','Булгаков М.А.',500)]
#
# try:
#     file3 = open('out.bin','wb')
#     try:
#         pickle.dump(books,file3)
#     finally:
#         file3.close()
# except FileNotFoundError:
#     print('no')
#
# try:
#     file3 = open('out.bin','rb')
#     try:
#         bs = pickle.load(file3)
#          print(bs)
#     finally:
#         file3.close()
# except FileNotFoundError:
#     print('no')

# import os
# # os.rename('13HW.py','HW13.py')
# # print('awda', os.getcwd())
#
# # os.mkdir('folder1')
# # os.chdir('folder1')
# # # os.chdir('..')
# # os.makedirs('nested111/nested222/nested333/')
#
# os.removedirs('folder/nested11/nested22/nested33')



# В файле, в одну строку записаны слова и числа через пробел или _ найти сумму всех чисел.
# with open('13HW.txt') as f:
#     s = f.readline()
#     print(s)
#
# sum = 0
# for i in s:
#     if i.isdigit():
#         i = int(i)
#         sum += i
# print(sum)

#Файл содержит числа и буквы. Каждый записан в отдельной строке.
# Нужно считать содержимое в список так, чтобы сначала шли числа по возрастанию,
# а потом слова по возрастанию их длины.
# with open('13HW.txt') as f:
#     s = f.readlines()
#     print(s)
# a = s[-1]
# s = s[:-1]
# b = []
# for i in s:
#     i = i[:-1]
#     b.append(i)
# b.append(a)
# print(b)
# c =[]
# d = []
# for i in b:
#     if i.isalpha():
#         i = str(i)
#         d.append(i)
#     if i.isdigit():
#         i = int(i)
#         c.append(i)
# d.sort()
# c.sort()
# v = c + d
# print(v)


#Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.

# f = open('13,1HW.txt','w')
# while True:
#     s = input()
#
#     if s == '':
#         break
#     f.write(s + '\n')
# f.close()

# создаете форму регистрации
# есть форма имени (длинна более 5 символов), любое имя короче 6 символов является недействительным,
# напишите код, что бы принемать имя в качестве входных данных и вызывать исключения если имя недействительно,
# выводя на экран "InvalidName" и выводить "AccountCreated" если имя действительно
# try: raise except
try:
    a = input('имя ')
    if len(a) < 5:
        raise ValueError
except:
    print('InvalidName')
else:
    print('AccountCreated')
