import pytest
import uuid
from src.models.repositories.links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler


db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="Test with interation with db")
def test_registry_link():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    link_infos = {
        'id': str(uuid.uuid4()),
        'trip_id': trip_id,
        'link': "somelink.com",
        'title': "Hotel"
    }

    link_repository.registry_link(link_infos)

@pytest.mark.skip(reason='Test with interation with db')
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    links = link_repository.find_links_from_trip(trip_id)
    print(links)
    
    assert isinstance(links, list)
    assert isinstance(links[0], tuple)
