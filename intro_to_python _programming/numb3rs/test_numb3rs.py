import numb3rs
from numb3rs import validate


def test_valid_ip():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True


def test_invalid_ip():
    assert validate("256.256.256.256") == False
    assert validate("192.168.1.256") == False
    assert validate("192.168.1.-1") == False
    assert validate("192.168.1.1.1") == False
    assert validate("192.168.1") == False
    assert validate("192.168.1.a") == False
    assert validate("192.168..1") == False
    assert validate("...") == False
    assert validate("1234.123.123.123") == False
    assert validate("192.168.1.01") == True  # Leading zeroes are acceptable


def test_edge_cases():
    assert validate("") == False
    assert validate(" ") == False
    assert validate("192.168.1. 1") == False  # Space inside the IP
    assert validate(" 192.168.1.1") == False  # Leading space
    assert validate("192.168.1.1 ") == False  # Trailing space
