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
        print(f"Имя фигуры - {self.__class__.__name__}")
        return f"Периметр равен = {self.perimeter()}\nПлощадь равна = {self.area()}"

    def check_args(self, *args):
        for v in args:
            if type(v) not in (int, float):
                raise ValueError(f"Неверный тип данных {self.__class__.__name__}!")
            if v < 0:
                raise ZeroDivisionError(f"Введенное значение {self.__class__.__name__} меньше 0!")

class Polygon(Figure):
    def __init__(self, side_a):
        self.sides = side_a
        self.check_args(self.sides)

    def area(self):
        return (13 * self.sides**2)/(4*math.tan(math.pi/13))

    def perimeter(self):
        return 13 * self.sides

class Triangle(Figure):
    def __init__(self, corner_a, corner_b, side_1, side_2, side_3):
        self.corners = (corner_a, corner_b)
        self.check_args(*self.corners)
        self.sides = (side_1, side_2, side_3)
        self.check_args(*self.sides)


    def area(self):
        return (self.sides[0] ** 2 * math.sin(180 - self.corners[0] - self.corners[1]) * math.sin(self.corners[1])) / (2 * math.sin(self.corners[0]))

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    print('Студент Караулов Дмитрий Алексеевич, вариант №4')
    side_polygon = float(input('Введите сторону правильного 13-многоугольника a = '))
    corner_a = float(input('Введите первый угол = '))
    corner_b = float(input('Введите второй угол = '))
    side_1 = float(input('Введите первую сторону = '))
    side_2 = float(input('Введите вторую сторону = '))
    side_3 = float(input('Введите третью сторону = '))
    figures = [Polygon(side_polygon), Triangle(corner_a, corner_b, side_1, side_2, side_3)]
    for i in figures:
        print(i.calculator())