from simple_intrest import simple_interest


def test_normal():
    assert simple_interest(1000, 5, 2) == 100


def test_zero_rate():
    assert simple_interest(1000, 0, 3) == 0


def test_zero_time():
    assert simple_interest(1000, 7, 0) == 0


def test_decimal():
    assert simple_interest(1000, 2.5, 2) == 50