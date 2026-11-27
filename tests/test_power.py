from calc.ops import power


def test_power():
    assert power(2, 3) == 8
    assert power(2, -1) == 0.5
    assert power(5, 0) == 1
