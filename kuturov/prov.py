# -*- coding: cp1251 -*-


from math import sqrt


class Hypotenuse:

    def __init__(self, cathetus_a: float = 0, cathetus_b: float = 0):
        self.cathetus_a = cathetus_a
        self.cathetus_b = cathetus_b

    @property
    def cathetus_a(self):
        return self._cathetus_a

    @cathetus_a.setter
    def cathetus_a(self, cathetus_a):
        if cathetus_a < 0:
            raise ValueError('Число не может быть отрицательным')
        self._cathetus_a = cathetus_a

    @property
    def cathetus_b(self):
        return self._cathetus_b

    @cathetus_b.setter
    def cathetus_b(self, cathetus_b):
        if cathetus_b < 0:
            raise ValueError('Число не может быть отрицательным')
        self._cathetus_b = cathetus_b

    def __str__(self):
        return f'Длинна прямоугольного треугольника со строной a = {self._cathetus_a} и стороной b = {self._cathetus_b} катета равна = {sqrt(self._cathetus_a ** 2 + self._cathetus_b ** 2)}'


def main():
    a, b = float(input('Введите первый катет: ')), float(input('Введите второй катет: '))
    hyp = Hypotenuse(cathetus_a=a, cathetus_b=b)
    print(hyp)


main()
