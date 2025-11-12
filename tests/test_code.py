from src.code import up_first

def test_up_first():
    assert up_first("hello") == "Hello"
    assert up_first("Hello") == "Hello"

def test_up_first_empty():
    assert up_first("") == ""
