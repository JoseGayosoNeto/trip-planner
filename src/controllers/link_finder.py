from typing import Dict
from src.models.repositories.links_repository import LinksRepository


class LinkFinder:
    
    def __init__(self, links_repository: LinksRepository) -> None:
        self.__links_repository = links_repository

    def find(self, trip_id: str) -> Dict:
        try:
            links = self.__links_repository.find_links_from_trip(trip_id)
            
            formatted_links = []
            for link in links:
                formatted_links.append({
                    "id": link[0],
                    "trip_id": link[1],
                    "url": link[2],
                    "description": link[3],
                })
            
            return {
                "body": {"links": formatted_links},
                "status_code": 200,
            }
        
        except Exception as e:
            return {
                "body": {"error": "Bad Request", "message": str(e)},
                "status_code": 400,
            }
