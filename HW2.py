# #Задача №1: Определить, является ли год високосным
# year = int(input('Введите год: '))
# if year % 4 == 0 and year % 100 !=0 or year % 400 ==0:
#     print('Високосный')
# else:
#     print('Невисокосный')

# Задача №2: Определить существование треугольника и его тип
#
# AB = int(input('Первая сторона:'))
# BC = int(input('Вторая сторона:'))
# AC = int(input('Третья сторона:'))
# while AB + BC < AC or AB + AC < BC or BC + AC < AB:
#     print('Треугольник не существует')
#     AB = int(input('Первая сторона:'))
#     BC = int(input('Вторая сторона:'))
#     AC = int(input('Третья сторона:'))
#
# print('Треугольник существует')
#
# if AB**2 == BC**2 + AC**2 or BC**2 == AB*22 + AC**2 or AC**2 == AB**2 + BC**2:
#     print('Треугольник прямоугольный')
# elif AB**2 < BC**2 + AC**2 or BC**2 < AB*22 + AC**2 or AC**2 < AB**2 + BC**2:
#     print('Треугольник остроугольный')
# else:
#     print('Треугольник тупоугольный')
# if AB == BC and AB != AC or BC == AC and BC !=AB or AB == AC and AB !=BC:
#     print('Треугольник равнобедренный')
# elif AB != BC and AB != AC and BC != AC:
#     print('Треугольник разносторонний')
# else:
#     print('Треугольник равносторонний')

# №Задача №3: Определить принадлежность точки кругу с
# центром в начале координат.
# Вводятся координаты (x,y) точки и радиус круга r.
# Определить принадлежит ли данная точка кругу, если
# его центр находится в начале координат.

# x = float(input('x = '))
# y = float(input('y = '))
# r = float(input('радиус:'))
# from math import sqrt
# g = sqrt(x**2 +y**2)
# if g <= r:
#     print('принадлежит')
# else:
#     print('не принадлежит')

# Задача №4: Творческое задание
# Придумать свою задачу на тему занятия. Обязательно
# использовать несколько вложений if-else(elif)
# # #Выбор квартиры
district = str(input('Выберите район: '))

while district != 'Московский' and district != 'Центральный' and district != 'Ленинский':
    print('Такого района нет')
    district = str(input('Выберите район: '))
if district == 'Московский':
    print('В этом районе квартиры от 300$')
if district == 'Центральный':
    print('В этом районе квартиры от 400$')
if district == 'Ленинский':
    print('В этом районе квартиры от 500$')
solution = str(input('Устраевает ли цена? '))
while solution == 'Нет' or solution == 'нет':
    district = str(input('Выберите район: '))

rooms = int(input('Сколько комнат? '))
if rooms == 1 and district == 'Моссковский':
    print('цена 300$')
if rooms == 2 and district == 'Моссковский':
    print('цена 320$')
if rooms == 3 and district == 'Моссковский':
    print('цена 350$')
if rooms == 1 and district == 'Центральный':
    print('цена 400$')
if rooms == 2 and district == 'Центральный':
    print('цена 420$')
if rooms == 3 and district == 'Центральный':
    print('цена 450$')
if rooms == 1 and district == 'Ленинский':
    print('цена 500$')
if rooms == 2 and district == 'Ленинский':
    print('цена 520$')
if rooms == 3 and district == 'Ленинский':
    print('цена 550$')