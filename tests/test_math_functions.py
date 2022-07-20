from src import math_functions
import pytest


@pytest.mark.number
def test_add():
    assert math_functions.add(7, 3) == 10
    assert math_functions.add(7) == 9


@pytest.mark.number
def test_product():
    assert math_functions.product(5, 5) == 25
    assert math_functions.product(5) == 10


@pytest.mark.strings
def test_add_strings():
    result = math_functions.add('Hello', "World")
    assert result == "HelloWorld"
    assert type(result) is str
    assert "Hello" in result


@pytest.mark.strings
@pytest.mark.skip(reason="no ejecutar esto")
def test_product_strings():
    assert math_functions.product("Hello ", 3) == "Hello Hello Hello "
    result = math_functions.product("Hello ")
    assert result == "Hello Hello "
    assert type(result) is str
    assert "Hello" in result
