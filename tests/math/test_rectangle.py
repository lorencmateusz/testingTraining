"""
Test all the implemented functions of rectangle class
"""

from main.math import Rectangle


class TestRectangle:
    def test_circumference(self):
        test_rectangle = Rectangle(3, 5)

        circumference = test_rectangle.circumference()

        assert circumference == 16

    def test_area(self):
        test_rectangle = Rectangle(3, 5)

        area = test_rectangle.area()

        assert area == 15

