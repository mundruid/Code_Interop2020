def test_find_power_two_error():
    assert find_power_two(12) == "Error"

def test_find_power_two_number():
    assert find_power_two(16) == 4

def test_find_power_two_extreme():
    assert find_power_two(0) == 0

def test_find_power_two_negative():
    assert find_power_two(-4) == "Error"