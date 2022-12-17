# -*- coding: cp1251 -*-

import abc
import math


class Figure(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass

    def calculator(self):
        print(f"______{self.__class__.__name__}______")
        return f"�������� ����� = {self.perimeter()}\n������� ����� = {self.area()}"

    def check_args(self, *args):
        for v in args:
            if type(v) not in (int, float):
                raise ValueError(f"�������� ��� ������ {self.__class__.__name__}!")
            if v < 0:
                raise ZeroDivisionError(f"��������� �������� {self.__class__.__name__} ������ 0!")

class Polygon(Figure):
    def __init__(self, side_a):
        self.sides = side_a
        self.check_args(self.sides)

    def area(self):
        return (3 * self.sides**2)/(4*math.tan(math.pi/3))

    def perimeter(self):
        return 3 * self.sides

class Ellipse(Figure):
    def __init__(self, side_a, side_b):
        self.sides = (side_a, side_b)
        self.check_args(*self.sides)

    def area(self):
        return math.pi * ((self.sides[0]*self.sides[1])/4)

    def perimeter(self):
        return 2 * math.pi * math.sqrt((self.sides[0]**2 + self.sides[1]**2)/8)

if __name__ == '__main__':
    print('������� �������, ������� �5')
    side_polygon = int(input('������� ������� ����������� 3-�������������� a = '))
    long_axis = int(input('������� ������� ��� ������ D = '))
    short_axis = int(input('������� �������� ��� ������ d = '))
    figures = [Polygon(side_polygon), Ellipse(long_axis, short_axis)]
    for i in figures:
        print(i.calculator())
