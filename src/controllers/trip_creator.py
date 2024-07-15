import uuid
from typing import Dict
from src.drivers.email_sender import send_email
from src.ethereal_email_client.client.create_email import account_instance
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.users_repository import UsersRepository

# Business Rules
class TripCreator:
    
    def __init__(self, trip_repository: TripsRepository, emails_repository: EmailsToInviteRepository, users_repository: UsersRepository) -> None:
        self.__trip_repository = trip_repository
        self.__emails_repository = emails_repository
        self.__users_repository = users_repository

    def create(self, body) -> Dict:
        try:
            emails = body.get('emails_to_invite')
            owner_email = body.get('owner_email')
            owner_name = body.get('owner_name')
            trip_id = str(uuid.uuid4())
            check_owner_email = self.__users_repository.find_user_by_email(owner_email)
            check_owner_name = self.__users_repository.find_user_by_name(owner_name)
            if check_owner_email and check_owner_name:
                trip_infos = {
                    **body,
                    'id': trip_id,
                    'owner_email': owner_email,
                    'owner_name': owner_name,
                }
                
                self.__trip_repository.create_trip(trip_infos)
                
                if emails:
                    for email in emails:
                        self.__emails_repository.registry_email({
                            "email": email,
                            "trip_id": trip_id,
                            "id": str(uuid.uuid4()),
                        })
                
                account = account_instance.get_account()
                send_email(
                    to_addrs=[body['owner_email']],
                    body=f'http://localhost:3000/trips/{trip_id}/confirm',
                    account_infos=account,
                )

                return {
                    "body": {"id": trip_id,},
                    "status_code": 201
                    
                }
            else:
                return {
                    "body": {"error": "Owner credentials not found."},
                    "status_code": 404,
                }
        
        except Exception as e:
            return {
                "body": {
                    "error": "Bad Request",
                    "message": str(e),
                },
                "status_code": 400,
            }