import pytest
from modules.common.database import Database

@pytest.mark.database
def test_get_user_by_name():
    db = Database()
    name = 'Stepan'
    address = 'Stepana Bandery str, 2'
    city = 'Kyiv'  

    user = db.get_user_by_name(name)

   
    print(user)
    
    assert user[0][0] == name
    assert user[0][2] == city
    assert user[0][1] == address

@pytest.mark.database
def test_get_user_by_name_with_exception_error():
    with pytest.raises(Exception):
        db = Database()

        db.get_user_by_name('')

@pytest.mark.database
def test_get_user_by_name_with_type_error():
    with pytest.raises(TypeError):
        db = Database()

        db.get_user_by_name(4)

@pytest.mark.database
def test_get_user_by_id():
    db = Database()
    id = 1

    user = db.get_user_by_id(id)

    print(user)

    assert user[0][0] == id
    

@pytest.mark.database
def test_get_user_by_id_with_exception_error():
    with pytest.raises(Exception):
        db = Database()

        db.get_user_by_id('')

@pytest.mark.database
def test_get_user_by_id_with_type_error():
    with pytest.raises(TypeError):
        db = Database()

        db.get_user_by_id('name')


@pytest.mark.database
def test_customers_insert():
    db = Database()
    db.insert_customers(3, 'Vika', 'Nuzhniy Val', 'Kyiv', 3478, 'Ukraine')
    user = db.get_user_by_id(3)

    assert user[0][0] == 3     