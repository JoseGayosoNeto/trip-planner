from typing import Dict
from src.models.repositories.trips_repository import TripsRepository

class TripFinder:
    
    def __init__(self, trips_repository: TripsRepository) -> None:
        self.__trips_repository = trips_repository

    def find_trip_details(self, trip_id: str) -> Dict:
        try:
            trip = self.__trips_repository.find_trip_by_id(trip_id)
            if not trip:
                raise ValueError("Trip not found")

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
        except Exception as e:
            return {
                "body": {"error": "Bad Request", "message": str(e)},
                "status_code": 400,
            }
        
