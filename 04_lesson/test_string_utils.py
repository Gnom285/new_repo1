
import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_data, expected",[
    ("     skypro", "skypro"),
    ("hello", "hello"),
    (" space ","space "),
])
def test_trim_positive(utils, input_data, expected):
    assert utils.trim(input_data) == expected



@pytest.mark.negative
def test_trim_none(utils):
    assert utils.trim(None) is None 


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol", [
    ("Skypro", "S"),
    ("Skypro", "y"),
    ("Hello", "o"),
])
def test_contains_positive( utils, string, symbol):
    assert utils.contains(string, symbol) is True


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol", [
    ("Skypro", "U"),
    ("Skypro", "s"),
    (None, "S"),
])
def test_contains_negative(utils, string, symbol):
    assert utils.contains(string, symbol) is False



@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("Skypro", "k", "Sypro"),
    ("Skypro", "pro", "Sky"),
    ("banana", "a", "bnn"),
])
def test_delete_symbol_positive(utils, string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected



@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("Skypro", "z", "Skypro"),
    ("", "a", ""),
    (None, "a", None),
])
def test_delete_symbol_negative(utils, string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected



