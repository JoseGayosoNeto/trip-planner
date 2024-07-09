import pytest
import uuid
from datetime import datetime, timedelta
from typing import Tuple
from src.models.repositories.trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()

trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="Test with interation with the db")
def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    
    trip_infos = {
        "id": trip_id,
        "destination": "Test Place",
        "start_date": datetime.strptime("01-01-2024", "%m-%d-%Y"),
        "end_date": datetime.strptime("01-01-2024", "%m-%d-%Y") + timedelta(days=5),
        "owner_name": "Test Owner",
        "owner_email": "testowner@email.com"
    }

    trips_repository.create_trip(trip_infos)

@pytest.mark.skip(reason="Test with interation with the db")
def test_find_trip_by_id() -> Tuple:
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    
    trip = trips_repository.find_trip_by_id(trip_id)
    print(trip)

@pytest.mark.skip(reason="Test with interation with the db")
def test_update_trip_status():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    
    trips_repository.update_trip_status(trip_id)
