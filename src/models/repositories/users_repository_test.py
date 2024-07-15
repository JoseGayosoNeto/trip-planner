import pytest
import random
import uuid
from string import ascii_letters, digits
from werkzeug.security import generate_password_hash, check_password_hash
from src.models.repositories.users_repository import UsersRepository
from src.models.settings.db_connection_handler import db_connection_handler


db_connection_handler.connect()
user_id = str(uuid.uuid4())
user_email = f'{''.join(random.choices(population=ascii_letters+digits, k=10))}@email.com'
user_name = ''.join(random.choices(population=ascii_letters, k=10))
pwhash = generate_password_hash(password="Test Password")

@pytest.mark.skip(reason='Test with interation with db.')
def test_create_user():
    conn = db_connection_handler.get_connection()
    users_repository = UsersRepository(conn)
    
    user_infos = {
        'id': user_id,
        'name': user_name,
        'email': user_email,
        'password': pwhash,
        'is_admin': 1,
    }
    
    users_repository.create_user(user_infos)

@pytest.mark.skip(reason='Test with interation with db.')
def test_find_user_by_id():
    conn = db_connection_handler.get_connection()
    users_repository = UsersRepository(conn)
    
    user = users_repository.find_user_by_id(user_id)
    print(user)
    
    assert check_password_hash(pwhash=pwhash, password="Test Password") == True
    assert user[0] == user_id
    assert user[1] == user_name
    assert user[2] == user_email
    assert user[4] == 1

@pytest.mark.skip(reason='Test with interation with db.')
def test_find_user_by_email():
    conn = db_connection_handler.get_connection()
    users_repository = UsersRepository(conn)

    user = users_repository.find_user_by_email(user_email)
    print(user)

    assert check_password_hash(pwhash=pwhash, password="Test Password") == True
    assert user[0] == user_id
    assert user[1] == user_name
    assert user[2] == user_email
    assert user[4] == 1

@pytest.mark.skip(reason='Test with interation with db.')
def test_find_user_by_name():
    conn = db_connection_handler.get_connection()
    users_repository = UsersRepository(conn)
    
    user = users_repository.find_user_by_name(user_name)
    print(user)

    assert check_password_hash(pwhash=pwhash, password="Test Password") == True
    assert user[0] == user_id
    assert user[1] == user_name
    assert user[2] == user_email
    assert user[4] == 1
