import math


def find_power_of_two(number):
    if not math.sqrt(number).is_integer():
        return "Error"
    else:
        return math.sqrt(number)


def test_find_power_of_two_error():
    assert find_power_of_two(12) == "Error"


def test_find_power_of_two_number():
    assert find_power_of_two(16) == 4


def test_find_power_of_two_extreme():
    assert find_power_of_two(0) == 0


def test_find_power_of_two_negative():
    assert find_power_of_two(-4) == "Error"


if __name__ == "__main__":
    pass
