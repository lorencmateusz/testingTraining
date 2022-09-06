"""
Test all the implemented functions of ExtensiveComputationFigure class.
Use patching to:
1. make circumference function not to take 10 second to execute
2. control the value of a and b - test different execution paths with specific values

Do not change the implementation of the ExtensiveComputationFigure class itself
"""

import pytest
from unittest.mock import patch
import random
from main import math
from main.math import ExtensiveComputationFigure


class MockExtensiveComputationFigure(math.ExtensiveComputationFigure):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b


class TestExtensiveComputationFigure:

    def test_circumference(self, monkeypatch):
        monkeypatch.setattr(math.time, "sleep", lambda x: 0)
        test_figure = math.ExtensiveComputationFigure()

        circumference = test_figure.circumference()

        assert circumference == 100

    @patch("main.math.random.randint")
    def test_area(self, randint):
        # monkeypatch.setattr(math, "ExtensiveComputationFigure", MockExtensiveComputationFigure)
        randint.side_effect = [1, 2]
        test_figure = ExtensiveComputationFigure()

        area = test_figure.area()

        assert area == 1
