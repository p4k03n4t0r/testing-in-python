import divide


def test_division_is_positive() -> None:
    assert divide.get_random_division() >= 0