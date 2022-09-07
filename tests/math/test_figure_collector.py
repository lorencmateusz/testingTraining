"""
Test the functions of FigureCollector class:
1. circumference for zero squares
2. circumference for one square
3. circumference for two squares
4. circumference for multiple "subclasses" of Figure class (using mock with all the needed functions)

1. area for zero squares
2. area for one squares
3. area for two squares
4. area for multiple "subclasses" of Figure class (using mock with all the needed functions)

"""
import pytest
from main.math import FigureCollector, Figure, Rectangle


class MockSquare(Figure):
    def __init__(self, a):
        self.a = a

    def circumference(self):
        return 4 * self.a

    def area(self):
        return self.a**2


square_one = MockSquare(1)


@pytest.fixture()
def a():
    return FigureCollector()


def mock_figure_adder(a, figures_count):
    sqr = Rectangle(1, 1)
    for i in range(figures_count):
        a.add_figure(sqr)


class TestFigureCollector:
    @pytest.mark.parametrize("figures_count, expected", [(0, 0), (1, 4), (2, 8)])
    def test_circumference_square(self, a, figures_count, expected):
        mock_figure_adder(a, figures_count)

        one_square_one_circumference = a.circumference()

        assert one_square_one_circumference == expected

    @pytest.mark.parametrize("figures_count, expected", [(1, 1), (2, 2), (3, 3)])
    def test_area_square(self, a, figures_count, expected):
        mock_figure_adder(a, figures_count)

        one_square_one_area = a.area()

        assert one_square_one_area == expected

    def test_circumference_custom_figure(self):
        pass

    def test_area_custom_figure(self):
        pass

