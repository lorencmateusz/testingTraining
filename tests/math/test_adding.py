from main.math import add

"""
Simple test case for  adding numbers
"""


class TestAdding:
    def test_sum_of_argument_is_correct(self):
        x = 3
        y = 5

        z = x + y

        assert z == 8
