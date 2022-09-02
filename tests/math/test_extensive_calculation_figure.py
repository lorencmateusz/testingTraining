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
import time
from main.math import ExtensiveComputationFigure





class MockExtensiveComputationFigure(ExtensiveComputationFigure):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b


class TestExtensiveComputationFigure:

    def test_circumference(self, monkeypatch):
        monkeypatch.setattr(time, "sleep", lambda x: 0)
        test_figure = ExtensiveComputationFigure()

        circumference = test_figure.circumference()

        assert circumference == 100

    def test_area(self, monkeypatch):
        def mock_random(x, y):
            return 3
        monkeypatch.setattr(random, "randint", mock_random)

        test_figure = ExtensiveComputationFigure()

        area = test_figure.area()

        assert area == 15
