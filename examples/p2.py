import math


def find_power_of_two(number):
    if number % 2 != 0:
        return "Error"
    else:
        return math.sqrt(number)


if __name__ == "__main__":
    pass
