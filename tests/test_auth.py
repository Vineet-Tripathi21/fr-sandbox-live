from calc.auth import check_token


def test_check_token():
    assert check_token("abc", "abc")
    assert not check_token("abc", "abd")
