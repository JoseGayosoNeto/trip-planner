from typing import Dict
from src.models.repositories.users_repository import UsersRepository


class UserFinder:

    def __init__(self, users_repository: UsersRepository) -> None:
        self.__users_repository = users_repository

    def find_user_from_id(self, user_id: str) -> Dict:
        try:
            user = self.__users_repository.find_user_by_id(user_id)
            if not user:
                raise ValueError("User not found.")

            return {
                "body": {
                    "id": user[0],
                    "name": user[1],
                    "email": user[2],
                    "is_admin": user[4],
                }
            }
        except Exception as e:
            return {
                "body": {"error": "Bad Request", "message": str(e)},
                "status_code": 400,
            }

    def find_user_from_email(self, user_email: str) -> Dict:
        try:
            user = self.__users_repository.find_user_by_email(user_email)
            if not user:
                raise ValueError("User not found.")

            return {
                "body": {
                    "id": user[0],
                    "name": user[1],
                    "email": user[2],
                    "is_admin": user[4],
                }
            }
        except Exception as e:
            return {
                "body": {"error": "Bad Request", "message": str(e)},
                "status_code": 400,
            }
