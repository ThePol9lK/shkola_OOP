# -*- coding: utf-8 -*-
import math


class Geometric:

    def __init__(self, num_1: float = 0, num_2: float = 0):
        self.num_1 = num_1
        self.num_2 = num_2
        self.result = 0

    def calculation(self):
        self.result = abs(math.sqrt(self.num_1 * self.num_2))
        return self.result

    def __str__(self):
        return f'Значение средне среднее геометрического модулей 2 чисел = {self.result}'


def main():
    a, b = float(input('Введите первое число: ')), float(input('Введите второе число: '))
    geo = Geometric(num_1=a, num_2=b)
    geo.calculation()
    print(geo)


main()
