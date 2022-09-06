from abc import ABC, abstractmethod
import random
import time
from typing import List


def add(x, y):
    return x + y


class Figure(ABC):

    @abstractmethod
    def circumference(self):
        pass

    @abstractmethod
    def area(self):
        pass


class ExtensiveComputationFigure(Figure):

    def __init__(self):
        self.a = random.randint(50, 100)
        self.b = random.randint(1, 55)

    def circumference(self):
        time.sleep(10)
        return 100

    def area(self):
        if self.a > self.b:
            return self.a - self.b
        else:
            return self.b - self.a


"""
Fill out the implementation
"""


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def circumference(self):
        return 2 * self.a + 2 * self.b

    def area(self):
        return self.a * self.b


class FigureCollector:

    def __init__(self):
        self.figures: List[Figure] = []

    def foo(self):
        for figure in self.figures:
            figure.area()

    def add_figure(self, figure: Figure):
        self.figures.append(figure)

    def circumference(self):
        return sum([figure.circumference() for figure in self.figures])

    def area(self):
        return sum([figure.area() for figure in self.figures])

    def print_list(self):
        print(self.figures)


a = Rectangle(1, 1)
x = FigureCollector()
x.add_figure(a)

print(x.area())
