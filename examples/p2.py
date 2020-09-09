import math


def find_power_of_two(number):
    if number < 0:
        return "Error"
    elif not math.sqrt(number).is_integer():
        return "Error"
    else:
        return math.sqrt(number)


if __name__ == "__main__":
    pass
