import pytest
from src.calculations import area_of_circle, get_nth_fibonacci


def test_area_of_circle_negative_radius_raises():
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        area_of_circle(-1)


def test_get_nth_fibonacci_negative_raises():
    with pytest.raises(ValueError, match="n cannot be negative"):
        get_nth_fibonacci(-1)


def test_get_nth_fibonacci_base_cases():
    assert get_nth_fibonacci(0) == 0
    assert get_nth_fibonacci(1) == 1