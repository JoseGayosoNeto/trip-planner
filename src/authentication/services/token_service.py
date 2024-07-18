from datetime import timedelta
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
from src.models.repositories.users_repository import UsersRepository

class RefreshTokenService:
    
    def __init__(self, users_repository: UsersRepository) -> None:
        self.__users_repository = users_repository

    def create_new_valid_token(self):
        try:
            userid_token = get_jwt_identity()
            user = self.__users_repository.find_user_by_id(userid_token)
            access_token = create_access_token(
                identity=userid_token,
                expires_delta=timedelta(hours=3),
                additional_claims={"roles":"admin", "user_id": userid_token} if user[4] == 1 else {"roles": "user", "user_id": userid_token}
            )
            refresh_token = create_refresh_token(
                identity=userid_token
            )
            
            return {
                "body": {
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                },
                "status_code": 200,
            }
        except Exception as e:
            return {
                "body": {"error": "Bad Request", "message": str(e)},
                "status_code": 400,
            }
        