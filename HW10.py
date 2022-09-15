
# Создайте словарь person, в котором будут присутствовать ключи name, age, city.
# Выведите значение возраста из словаря person

# person = dict(name= 'Anton',age = 24,city = 'Minsk')
# print(person['age'])


# Значениями словаря могут быть и списки.
# Создайте словарь с ключами BMW, Tesla и списками из 3х моделей в качестве значений.
# Выведите первое и последнее значения каждого из ключей.

# cars = dict([('BMW',(1,2,3)),('Tesla',(4,5,6))])
# print(cars['BMW'][0],'\n',cars['Tesla'][-1])
# cars1 = {'BMW':[1,2,3],'Tesla':[4,5,6]}
# print(cars1['BMW'][0],cars1['BMW'][-1],'\n',cars1['Tesla'][0],cars1['Tesla'][-1])

# d1 = {"a": 100, "b": 200, "c":300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# print(d1["b"] == d2["b"])

#Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.
# d1 = {"a": 100, "b": 200, "c":300}
# n=1
# for i in d1:
#     n*= d1[i]
# print(n)

#У вас есть словарь, где ключ – название продукта. Значение – список, который содержит цену и кол-во товара.
# Выведите через ‘’–’’ название – цену – количество.
# С клавиатуры вводите название товара и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном списке.

a = {'хлеб':[10,5],'мясо':[20,4],'молоко':[15,6]}
a1 = {'хлеб':[10,5],'мясо':[20,4],'молоко':[15,6]}
q = []
cost=1
all_cost = 0
for w in a.keys():
    while a[w][1] != 0:

        b = input('Что хотите купить?: ')
        if b == 'n':
            break
        elif b not in a.keys():
            print('Такого товара нет')
            continue
        c = int(input('Сколько?: '))

        if b in a.keys():
            if a[b][1] >= c:
                a[b][1] -= c
                cost = a[b][0] * c
                all_cost +=cost
                print(b, '-', c, '-', cost, 'руб')
                if a[b][1] == 0:
                    print(b, 'закончился')
            elif a[b][1] < c:
                print('Столько', b, 'нет')

        q.append(b)                     # список купленых продуктов (без повторений)
        for i in q:
            while q.count(i)>1:
                q.remove(i)

print('Весь товар скуплен \n Приходите еще!\n__________________________________________')

print('вы купили:')
for j in q:                                 #узнаю, сколько куплено каждого продукта
    print(j, a1[j][1]-a[j][1],'шт')
print('Всего потрачено:',all_cost,'руб.')


#Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
# чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями нашего словаря.

# a = ['key1','key2','key3','key4']
# b = ['value1','value2','value3','value4']
# c = dict(zip(a,b))
# print(c)


#Создайте словарь из строки 'pythonist' следующим образом:
# в качестве ключей возьмите буквы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку.

a = 'pythonist'
b =[]
d = []
for i in a:
    b.append(i)
for j in a:
    d.append(a.count(j))
c = dict(zip(b,d))
print(c)

# b = {i:a.count(i) for i in a}
# print(b)


# #Способы создания словарей
#
# # №1 с помощью литерала
# a = {'a':1,'b':2}
# print(a)
#
# # №2.1 с помощью функции dict
# b = dict(one=1,two=2)
# print(b['one'])
# # №2.2
# b2 = dict([('three',22),(2,33)])
# print(b2['three'])
#
# # №3 с помощью метода fromkays
# b3 = dict.fromkeys(['q','w'])
# print(b3)
# b3_2 = dict.fromkeys(['e','r'],(100,200))
# print(b3_2)
#
# # №4 с помощью генератора словарей
# d = {a1: a1**2 for a1 in range(10)}
# print(d)


# d = {1:1,2:2,3:3}
# d[10] = 2
# print(d)
# print(d[3])
# # d.clear()
# # print(d)
# a = d.copy()
# print(a)
# print(id(d), '\n',id(a)  )
# a[2] = 3**4
# print(d, a)


# d = {1:11,2:22,3:33}
# print(d.items(),'\n', d.keys(),'\n', d.values())
# MyDictionary= {}
# MyDictionary[0] = 'Apples'
# MyDictionary[2] = 'Mangoes'
# MyDictionary[3] = 20
# MyDictionary[-1] = 200
# MyDictionary[10] = 2000
# sorted(MyDictionary)
# print("\n3 elements have been added: ")
# # MyDictionary.pop(10,200)
# print(MyDictionary)

# d = {1:11,2:22,3:33}
# d1 = {4:44,5:55,6:66}
# d.update(d1)
# print(d,'\n',d1)


# d = {1:11,2:22,3:33}
# d1 = {4:44,5:55,6:66}
#
# del d[1]
# print(d)

# a = dict(i=i**3 for i in range(1,11)}
# print(a)
