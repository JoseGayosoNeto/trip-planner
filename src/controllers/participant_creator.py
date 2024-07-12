import uuid
from typing import Dict
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.participants_repository import ParticipantsRepository


class ParticipantCreator:
    
    def __init__(self, participants_repository: ParticipantsRepository,
                 emails_to_invite_repository: EmailsToInviteRepository) -> None:
        self.__participants_repository = participants_repository
        self.__emails_repository = emails_to_invite_repository

    def create(self, body, trip_id) -> Dict:
        try:
            participant_id = str(uuid.uuid4())
            emails_id = str(uuid.uuid4())

            emails_infos = {
                "id": emails_id,
                "trip_id": trip_id,
                "email": body['email'],
            }

            participant_infos = {
                'name': body['name'],
                'trip_id': trip_id,
                'emails_to_invite_id': emails_id,
                'id': participant_id,
            }
            
            self.__emails_repository.registry_email(emails_infos)
            self.__participants_repository.registry_participant(participant_infos)
            
            return {
                "body": {"id": participant_id},
                "status_code": 201,
            }

        except Exception as e:
            return {
                "body": {"error": "Bad Request", "message": str(e)},
                "status_code": 400,
            }
