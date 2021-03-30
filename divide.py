import random


def _divide(x: int, y: int) -> float:
    if y == 0:
        raise Exception("Can't divide by zero!")
    return x / y


def _get_random_positive() -> int:
    return random.randint(1, 100)


def get_random_division() -> float:
    a = _get_random_positive()
    b = _get_random_positive()
    return _divide(a, b)
