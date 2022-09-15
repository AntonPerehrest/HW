# # Создайте класс Example. В нём пропишите 3 (метода) функции.
#
class Example:
    # Две переменные задайте статически
    a = 2
    b = 3

    # Две переменные задайте динамически
    def __init__(self, r, t):
        self.r = r
        self.t = t

    ## Первая функция: создайте переменную и выведите её
    def func(self):
        self.a = 7
        print(self.a)

    # Вторая функция: верните сумму 2-ух глобальных переменных
    def func_1(self):
        return self.a + self.b


    # Третья функция: верните результат возведения первой динамической переменной во вторую динамическую переменную
    def func_2(self):
        return self.r ** self.t
    #Создайте объект класса
example = Example(4,2)
    # Напечатайте обе функци
print(example.func_1())
print(example.func_2())
    # Напечатайте переменную a
print(example.a)
example.func()



#Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв меньше или равно длине слова, выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.

# class Dz:
#
#     def __init__(self):
#         self.a = input('Введи: ')
#     def func(self):
#         if str(self.a).isdigit():
#             sum = 0
#             for i in self.a:
#                 if int(i) % 2 == 0:
#                     sum += int(i)
#             print(sum + len(self.a))
#
#         else:
#             gl = 0
#             spis_gl = []
#             sgl = 0
#             spis_sgl = []
#             for i in self.a:
#                 if i in 'eyuioa':
#                     gl += 1
#                     spis_gl.append(i)
#                 else:
#                     sgl += 1
#                     spis_sgl.append(i)
#             if gl * sgl <= len(self.a):
#                 print(spis_gl)
#             else:
#                 print(spis_sgl)
#
#
# p = Dz()
# p.func()



инкапсуляция
наследование
полиморфизм