# Создайте класс Circle (окружность). Для данного
# класса реализуйте ряд перегруженных операторов:
# ■ Проверка на равенство радиусов двух окружностей
# (операция = =);
# ■ Сравнения длин двух окружностей (операции >, <,
# <=,>=);
# ■ Пропорциональное изменение размеров окружности,
# путем изменения ее радиуса (операции + - += -=).
# import math
#
#
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def perimetr(self):
#         return 2 * math.pi * self.r
#
#     def area(self):
#         return math.pi * self.r**2
#
#     def __eq__(self, other):
#         return self.r == other.r
#
#     def __lt__(self, other):
#         return self.perimetr() < other.perimetr()
#
#     def __le__(self, other):
#         return self.perimetr() <= other.perimetr()
#
#     def __gt__(self, other):
#         return self.perimetr() > other.perimetr()
#
#     def __ge__(self, other):
#         return self.perimetr() >= other.perimetr()
#
#     def __add__(self, other):
#         if self.r + other < 0:
#             raise TypeError("Радиус не может быть отрицательным")
#         return Circle(self.r + other)
#
#     def __sub__(self, other):
#         if self.r - other < 0:
#             raise TypeError("Радиус не может быть отрицательным")
#         return Circle(self.r - other)
#
#     def __iadd__(self, other):
#         if self.r + other < 0:
#             raise TypeError("Радиус не может быть отрицательным")
#         self.r += other
#
#     def __isub__(self, other):
#         if self.r - other < 0:
#             raise TypeError("Радиус не может быть отрицательным")
#         self.r -= other
#
#
# a = Circle(3)
# b = Circle(6)
# c = Circle(3)
#
# print(a == b)
# print(a == c)
# print(a < b)
# print(b > a)
# print(a > b)
# print(b < a)
# print(a + 3 == b)
# print(a.perimetr() * 2 == (a + a.r).perimetr())

# Задание 2
# Создайте класс Complex (комплексное число). Более
# подробно ознакомиться с комплексными числами можно
# по ссылке.
# Создайте перегруженные операторы для реализации
# арифметических операций для по работе с комплексными
# числами (операции +, -, *, /).
# import math
#
#
# class Complex:
#
#     def __init__(self, real, image):
#         self.real = real
#         self.image = image
#
#     def __abs__(self):  # Модуль комплексного числа
#         return (self.real ** 2 + self.image ** 2) ** 0.5
#
#     def angle(self):  # угол между вещественной и мнимой частью
#         return math.atan(self.image/self.real) * 180/math.pi
#
#     def __add__(self, other):
#         new_r = self.real + other.real
#         new_i = self.image + other.image
#         return Complex(new_r, new_i)
#
#     def __iadd__(self, other):
#         self.real += other.real
#         self.image += other.image
#
#     def __sub__(self, other):
#         new_r = self.real - other.real
#         new_i = self.image - other.image
#         return Complex(new_r, new_i)
#
#     def __isub__(self, other):
#         self.real -= other.real
#         self.image -= other.image
#
#     def __mul__(self, other):
#         new_r = self.real * other.real - self.image * other.image
#         new_i = self.image * other.real + self.real * other.image
#         return Complex(new_r, new_i)
#
#     def __truediv__(self, other):
#         new_r = round((self.real * other.real + self.image * other.image)/(other.real ** 2 + other.image ** 2),2)
#         new_i = round((self.image * other.real - self.real * other.image)/(other.real ** 2 + other.image ** 2),2)
#         return Complex(new_r, new_i)
#
#     def __str__(self):
#         if self.image > 0:
#             return f'{self.real} + j{self.image}'
#         elif self.image < 0:
#             return f'{self.real} - j{self.image * -1}'
#         else:
#             return f'{self.real} '
#
#
# a = Complex(3, 4)
# b = Complex(5, 9)
#
# print(a + b)
#
# print(a - b)
#
# print(a * b)
#
# print(a / b)
# (2:25)
# Задание 3
# Вам необходимо создать класс Airplane (самолет).
# Проверка на равенство типов самолетов (операция
# = =);
# ■ Увеличение и уменьшение пассажиров в салоне са-
# молета (операции + - += -=);
# ■ Сравнение двух самолетов по максимально возмож
# ному количеству пассажиров на борту (операции >
# < <= >=).
# from abc import ABC, abstractmethod
#
#
# class Airplane(ABC):
#
#     def __init__(self, max_psngrs, psngrs, max_speed, named):
#         if psngrs > max_psngrs:
#             raise TypeError('Пассажиров не может быть больше максимального количества')
#         if psngrs <= 0 :
#             raise TypeError('Самолет не полетит без пассажиров')
#         self.max_psngrs = max_psngrs
#         self.psngrs = psngrs
#         self.max_speed = max_speed
#         self.named = named
#
#     @abstractmethod
#     def flying(self):
#         print('Not flying')
#
#     def __eq__(self, other):
#         return isinstance(self, type(other))
#
#     def __add__(self, other):
#         if self.psngrs + other > self.max_psngrs:
#             raise TypeError('Пассажиров не может быть больше максимального количества')
#         return self.__class__(self.max_psngrs, self.psngrs + other, self.max_speed, self.named)
#
#     def __iadd__(self, other):
#         if self.psngrs + other > self.max_psngrs:
#             raise TypeError('Пассажиров не может быть больше максимального количества')
#         self.psngrs += other
#
#     def __sub__(self, other):
#         if self.psngrs - other <= 0:
#             raise TypeError('Самолет не полетит без пассажиров')
#         return self.__class__(self.max_psngrs, self.psngrs - other, self.max_speed, self.named)
#
#     def __isub__(self, other):
#         if self.psngrs - other <= 0:
#             raise TypeError('Самолет не полетит без пассажиров')
#         self.psngrs -= other
#
#     def __lt__(self, other):
#         return self.max_psngrs < other.max_psngrs
#
#     def __le__(self, other):
#         return self.max_psngrs <= other.max_psngrs
#
#     def __gt__(self, other):
#         return self.max_psngrs > other.max_psngrs
#
#     def __ge__(self, other):
#         return self.max_psngrs >= other.max_psngrs
#
#
# class RegionalAir(Airplane):
#     def __init__(self, max_psngrs, psngrs, max_speed, named, flight_range):
#         super().__init__(max_psngrs, psngrs, max_speed, named)
#         self.flight_range = flight_range
#
#     def flying(self):
#         print(f'{self.named} flying not far')
#
#
# class IntercontinentalAir(Airplane):
#     def __init__(self, max_psngrs, psngrs, max_speed, named, flying_height):
#         super().__init__(max_psngrs, psngrs, max_speed, named)
#         self.flying_height = flying_height
#
#     def flying(self):
#         print(f'{self.named} flying too far')
#
#
# boeng1 = RegionalAir(200, 150, 380, 'Ту-150', 10000)
# boeng2 = RegionalAir(300, 200, 500, 'Ту-250', 3600)
# boeng3 = IntercontinentalAir(400, 250, 600, 'Ту-350', 3900)
#
# print(boeng1 == boeng2)
# print(boeng1 == boeng3)
# print(boeng1 > boeng2)
# print(boeng3 > boeng2)

# Задание 4
# Создать класс Flat (квартира). Реализовать перегру-
# женные операторы:
# ■ Проверка на равенство площадей квартир (операция
# ==);
# ■ Проверка на неравенство площадей квартир (опера-
# ция !=);
# ■ Сравнение двух квартир по цене (операции > < <= >=).

# class Flat:
#     def __init__(self, area, price):
#         self.area = area
#         self.price = price
#
#     def __eq__(self, other):
#         return self.area == other.area
#
#     def __ne__(self, other):
#         return self.area != other.area
#
#     def __lt__(self, other):
#         return self.price < other.price
#
#     def __le__(self, other):
#         return self.price <= other.price
#
#     def __gt__(self, other):
#         return self.price > other.price
#
#     def __ge__(self, other):
#         return self.price >= other.price




