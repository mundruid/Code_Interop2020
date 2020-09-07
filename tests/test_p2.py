import pytest

from examples import p2


class TestExamples:
    def test_find_power_two_error_odd(self):
        assert p2.find_power_of_two(13) == "Error"

    def test_find_power_two_error_even(self):
        assert p2.find_power_of_two(12) == "Error"

    def test_find_power_two_number(self):
        assert p2.find_power_of_two(16) == 4

    def test_find_power_two_extreme(self):
        assert p2.find_power_of_two(0) == 0

    def test_find_power_two_negative(self):
        assert p2.find_power_of_two(-4) == "Error"
