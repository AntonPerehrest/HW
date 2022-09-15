# class Car:
#     def __str__(self):
#         return 'Car class Object'
#
#     def start(self):
#         print('Двигатель заведен')
#
#
# car_a = Car()
# print(car_a)


# class Car:
#     def model(self):
#         return 'Car class Object'
#
#     def start(self):
#         print('Двигатель заведен')
#
#
# car_a = Car()
# print(car_a)


# class Phone:
#
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#
#
#     def check_sim(self, operator):
#         if self.model == 'aa' and operator == 'MTS':
#             print('Yes')
#
# # my_phone = Phone('red', 'aa')
# # my_phone.check_sim('MTS')
#
#     @staticmethod
#     def model_hash(model):
#         if model == 1:
#             return 11
#         elif model == '2':
#             return 22
#         else:
#             return None
#
# Phone.model_hash(1)
# my_phone = Phone('red', 'aa')
# print(my_phone.check_sim('MTS'))


# class Phone:
#
#     def __init__(self,os, color, model):
#         self.color = color
#         self.model = model
#         self.os = os
#
#
#     @classmethod
#     def toy_phone(cls, color):
#         toy_phone = cls(color, 'ToyPhone', None)
#         return toy_phone
#
#
# p = Phone('ios','Red', 'HTC')
# print(p.toy_phone('Green'))





class Human:

    default_name = 'No name'
    default_age = 0


    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age

        self.__money = 0
        self.__house = None


    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Money: {self.__money}')
        print(f'Hous: {self.__house}')

    @staticmethod
    def default_info():
        print(f'Default Name: {Human.default_name}')
        print(f'Default Age: {Human.default_age}')

    def earn_money(self,amount):
        self.__money += amount
        print(f'Earned {amount} money! Current value: {self.__money}')


    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print('Not enough money')


    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house


class House:

    def __init__(self, area, price):
        self.__area = area
        self.__price = price

    def final_price(self, discont):
        final_price = self.__price * (100 - discont)/100
        print(f'Final price: {final_price}')
        return final_price


class SmallHouse(House):
    default_area = 40
    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)

if __name__ =='__main__':

    Human.default_info()

    alex = Human('Sasha', 27)
    alex.info()

    small_house = SmallHouse(8_500)

    alex.buy_house(small_house, 5)

    alex.earn_money(5_000)
    alex.buy_house(small_house, 5)

    alex.earn_money(20_000)
    alex.buy_house(small_house, 5)
    alex.info()





# class Phone:
#
#     def __init__(self):
#         self.is_on = False
#
#     def turn_on(self):
#         self.is_on = True
#
#     def call(self):
#         if self.is_on:
#             print('Making call...')
#
# class MobilePhone(Phone):
#
#     def __init__(self):
#         super().__init__()
#         self.battary = 0
#
#     def charge(self, num):
#         self.battary = num
#         print(f'Charging battary up to ... {self.battary}%')
#
# print(dir(Phone))
# my_phone = MobilePhone()
# print(dir(my_phone))


# class Vehicle:
#     def vehicle_metod(self):
#         print('родительский')
#
# class Car(Vehicle):
#     def car_metod(self):
#         print('потомок')
#
# class Bike(Vehicle):
#     def bike_metod(self):
#         print('потомок')
#
# r = Vehicle()
# r.vehicle_metod()
#
# p_1 = Car()
# p_1.car_metod()
#
# p_2 = Bike()
# p_2.bike_metod()

