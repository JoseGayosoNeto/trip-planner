import uuid
from typing import Dict
from werkzeug.security import generate_password_hash
from src.models.repositories.users_repository import UsersRepository


class UserCreator:

    def __init__(self, users_repository: UsersRepository) -> None:
        self.__user_repository = users_repository

    def create(self, body) -> Dict:
        try:
            user_id = str(uuid.uuid4())
            password = body.get('password')
            
            user_infos = {
                **body,
                'id': user_id,
                'password': generate_password_hash(password),
            }
            self.__user_repository.create_user(user_infos)
            
            return {
                "body": {"id": user_id},
                "status_code": 201,
            }
        except Exception as e:
            return {
                "body": {"error": "Bad Request", "message": str(e)},
                "status_code": 400,
            }
