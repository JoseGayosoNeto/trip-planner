from datetime import timedelta
from typing import Dict
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import check_password_hash
from src.models.repositories.users_repository import UsersRepository


class AuthenticationService:

    def __init__(self, users_repository: UsersRepository) -> None:
        self.__users_repository = users_repository

    def login(self, body) -> Dict:
        try:
            email = body.get('email')
            password = body.get('password')
            
            user = self.__validate_password_hash(email, password)
            if user:
                access_token = create_access_token(
                    identity=user[0],
                    expires_delta=timedelta(hours=3),
                    additional_claims={"roles": "admin", "user_id": user[0]} if user[4] == 1 else {"roles": "user", "user_id": user[0]}
                )
                refresh_token = create_refresh_token(
                    identity=user[0],
                )
                
                return {
                    "body": {
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                        "message": "Successful Log in",
                    },
                    "status_code": 200,
                }
        except Exception as e:
            return {
                "body": {"error": "Bad Request", "message": str(e)},
                "status_code": 400,
            }
    
    def __validate_password_hash(self, user_email: str, user_password: str):
        user = self.__users_repository.find_user_by_email(user_email)
        if user and check_password_hash(user[3], user_password):
            return user
    
        raise ValueError("Invalid credentials.") 