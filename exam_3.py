# 1 Рекурсия. Возведение числа x в степень y\

# def num_ext(x,y):
#     if y == 1:
#         return x
#     elif y == 0:
#         return 1
#     else:
#         return x*num_ext(x, y-1)
# x = int(input('num: '))
# y = int(input('extent: '))
# print(num_ext(x,y))


# 2 Определить функцию, которая проверяет является ли строка, введенная пользователем, целым числом. Решение задачи сдать ссылкой на GitHub.

# def if_int(x):
#     try:
#         int(x)
#         return True
#     except ValueError:
#         return False
#
# x = input('Введи:')
# print(if_int(x))

# 3 Создайте класс IceCream (для заказа мороженого с добавкой или без),
# принимающий 1 аргумент при инициализации (отвечающий за добавку к мороженому).
# В этом классе реализуйте метод info_about_icecream(), выводящий на печать «Мороженное и {ДОБАВКА}»
# в случае наличия добавки, а иначе отобразится следующая фраза: «Обычное мороженое».

# class IceCream:
#     def __init__(self, dobavka):
#         if isinstance(dobavka, str):
#             self.dobavka = dobavka
#         else:
#             self.dobavka = None
#     def info_about_icecream(self):
#         if self.dobavka:
#             print(f'Мороженное и {self.dobavka}')
#         else:
#             print('Обычное мороженое')
#
# icecream_1 = IceCream(1)
# icecream_2 = IceCream('Nuts')
#
# icecream_1.info_about_icecream()
# icecream_2.info_about_icecream()


# 4 Инкапсуляция. Определить класс Car, который будет содержать конструктор,
# в котором будет инициализироваться private переменная maxprice,
# а также методы изменения и вывода максимальной стоимости машины.

class Car:
    def __init__(self, maxprice):
        self.__maxprice = maxprice

    def info(self):
        print(f'Car maxprice - {self.__maxprice}')
    #
    # def set_cost(self, maxprice):
    #     self.__maxprice = maxprice
    #
    #
    # def get_cost(self):
    #     return f'New cost - {self.__maxprice}'
    @property
    def price(self):
       return f'New car price - {self.__maxprice}'

    @price.setter
    def price(self, maxprice):
       self.__maxprice = maxprice


car = Car(10_000)
car.info()


car.price = 20_000
print(car.price)




#          !!!!!!!!!!!!!!!!!!          посмотреть декораторы для setter and getter      !!!!!!!!!!!!!!!!!!!

# 5 Создать класс Animal и определить в нем метод make_a_sound(). Метод должен вывоводить строку "Издает звук"
# Cоздать классы Cat и Dog с методами scratch() и dig() соответственно.
# Метод scratch должен выводить строку "Царапать мебель".
# Метод dig должен выводить строку "Рыть землю".
# в классах Cat и Dog переопределите метод make_a_sound() базового класса Animal.
# (Cat: make_a_sound() -> '<...>', Dog: make_a_sound() -> '<...>')

# class Animal:
#     def __init__(self):
#         pass
#
#     def make_a_sound(self):
#         print('Издает звук')
#
#
# class Cat(Animal):
#     def scratch(self):
#         print('Царапать мебель')
#
#     def dig(self):
#         print('Рыть землю')
#
#     def make_a_sound(self):
#         print('Мяукает')
#
#
# class Dog(Animal):
#     def scratch(self):
#         print('Царапать мебель')
#
#     def dig(self):
#         print('Рыть землю')
#
#     def make_a_sound(self):
#         print('Лает')
#
# cat = Cat()
# cat.make_a_sound()
#
# dog = Dog()
# dog.make_a_sound()


#new commit
#new commit

# list_of_keys = ['a', 'b', 'c', 'd']
# list_of_incidents = ["собака погналась за голубем и потерялась", "собака попала под машину",
#                              "собака подралась с другой собакой", "собака наелась из мусорки и отравилась"]
# all = dict(zip(list_of_keys, list_of_incidents))
#
# print(all['a'])

