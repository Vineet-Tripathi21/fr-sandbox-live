def add(a: float, b: float) -> float:
    return a + b


def sub(a: float, b: float) -> float:
    return a - b


def div(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def power(base: float, exp: int) -> float:
    if exp < 0:
        return 1 / power(base, -exp)
    return base**exp
