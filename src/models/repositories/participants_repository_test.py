import pytest
import uuid
from src.models.repositories.participants_repository import ParticipantsRepository
from src.models.settings.db_connection_handler import db_connection_handler


db_connection_handler.connect()
participant_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())
emails_to_invite_id = str(uuid.uuid4())

@pytest.mark.skip(reason="Test with interation with db")
def test_registry_participant():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participants_info = {
        "id": participant_id,
        "trip_id": trip_id,
        "emails_to_invite_id": emails_to_invite_id,
        "name": "Test Participant",
        "is_confirmed": 1
    }
    
    participants_repository.registry_participant(participants_info)

@pytest.mark.skip(reason="Test with interation with db")
def test_find_participants_from_trip():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    
    participants = participants_repository.find_participants_from_trip(trip_id)
    print(participants)

    assert isinstance(participants, list)

@pytest.mark.skip(reason="Test with interation with db")
def test_update_participant_status():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    
    participants_repository.update_participant_status(participant_id)
