import math


def find_power_of_two(number):
    if not math.sqrt(number).is_integer():
        return "Error"
    else:
        return math.sqrt(number)


if __name__ == "__main__":
    pass
