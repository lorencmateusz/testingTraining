from abc import ABC, abstractmethod
import random
from time import sleep
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
        sleep(10)
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
    pass


class FigureCollector:

    def __init__(self):
        self.figures: List[Figure] = []

    def add_figure(self, figure: Figure):
        self.figures.append(figure)

    def circumference(self):
        return sum([figure.circumference() for figure in self.figures])

    def area(self):
        return sum([figure.area() for figure in self.figures])
