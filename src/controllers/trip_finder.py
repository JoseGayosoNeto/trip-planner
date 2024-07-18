from flask_jwt_extended import get_jwt
from typing import Dict
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.users_repository import UsersRepository

class TripFinder:
    
    def __init__(self, trips_repository: TripsRepository, users_repository: UsersRepository) -> None:
        self.__trips_repository = trips_repository
        self.__users_repository = users_repository

    def find_trip_details(self, trip_id: str) -> Dict:
        try:
            trip = self.__trips_repository.find_trip_by_id(trip_id)
            trip_owner = self.__users_repository.find_user_by_name(trip[4])
            if not trip:
                raise ValueError("Trip not found")

            claims = get_jwt()
            if claims['user_id'] == trip_owner[0]:
                return {
                    "body": {
                        "id": trip[0],
                        "destination": trip[1],
                        "starts_at": trip[2],
                        "ends_at": trip[3],
                        "status": trip[6]
                    },
                    "status_code": 200,
                }
            else:
                print(trip_owner[0])
                print(claims['user_id'])
                print(claims['roles'])
                raise Exception("Token user didn't match with trip owner")
        except Exception as e:
            return {
                "body": {"error": "Bad Request", "message": str(e)},
                "status_code": 400,
            }
        
