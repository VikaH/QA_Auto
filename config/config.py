import pytest

@pytest.mark.check
def test_check_math():
    assert 7*7 == 49

@pytest.mark.check
def test_check_78():
    assert 7*8 == 56

# function to test: { 'age': 12, 'name': ''Vasya' }
@pytest.mark.check
def check_if_adult(user):
    if user['age'] >= 18:
        return True
    else:
        return False

@pytest.mark.check   
def test_check_if_adult():
    assert check_if_adult({ 'age': 19 }) == True