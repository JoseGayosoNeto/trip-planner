import uuid
from typing import Dict
from src.models.repositories.links_repository import LinksRepository


class LinkCreator:
    
    def __init__(self, link_repository: LinksRepository) -> None:
        self.__link_repository = link_repository

    def create(self, body, trip_id) -> Dict:
        try:
            link_id = str(uuid.uuid4())
            link_infos = {
                **body,
                "id": link_id,
                "trip_id": trip_id,
            }
            
            self.__link_repository.registry_link(link_infos)
            
            return {
                "body": {"id": link_id},
                "status_code": 201,
            }
        except Exception as e:
            return {
                "body": {"error": "Bad Request", "message": str(e)},
                "status_code": 400,
            }
