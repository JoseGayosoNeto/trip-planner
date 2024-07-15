from flask import jsonify, Blueprint, request

# Import Controllers
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer

from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder

from src.controllers.participant_creator import ParticipantCreator
from src.controllers.participant_finder import ParticipantFinder
from src.controllers.participant_confirmer import ParticipantConfirmer

from src.controllers.activity_creator import ActivityCreator
from src.controllers.activity_finder import ActivityFinder

# Import Repositories
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.participants_repository import ParticipantsRepository
from src.models.repositories.activities_repository import ActivitiesRepository
from src.models.repositories.users_repository import UsersRepository

# Import Connection
from src.models.settings.db_connection_handler import db_connection_handler

trips_routes_bp = Blueprint("trip_routes", __name__)

@trips_routes_bp.route('/trips', methods=['POST'])
def create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    users_repository = UsersRepository(conn)
    controller = TripCreator(trips_repository, emails_repository, users_repository)
    
    response = controller.create(request.json)
    
    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route('/trips/<trip_id>', methods=['GET'])
def get_trip(trip_id):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripFinder(trips_repository)
    
    response = controller.find_trip_details(trip_id)
    
    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route('/trips/<trip_id>/confirm', methods=['GET'])
def confirm_trip(trip_id):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripConfirmer(trips_repository)
    
    response = controller.confirm(trip_id)
    
    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route('/trips/<trip_id>/links', methods=['POST'])
def create_link(trip_id):
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)
    controller = LinkCreator(link_repository)
    
    response = controller.create(request.json, trip_id)
    
    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route('/trips/<trip_id>/links', methods=['GET'])
def get_trip_links(trip_id):
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)
    controller = LinkFinder(link_repository)
    
    response = controller.find(trip_id)
    
    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route('/trips/<trip_id>/invites', methods=['POST'])
def invite_to_trip(trip_id):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = ParticipantCreator(participants_repository, emails_repository)
    
    response = controller.create(request.json, trip_id)
    
    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route('/trips/<trip_id>/participants', methods=['GET'])
def get_participants(trip_id):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantFinder(participants_repository)
    
    response = controller.find_participants_from_trip(trip_id)
    
    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route('/participants/<participant_id>/confirm', methods=['PATCH'])
def confirm_participant(participant_id):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantConfirmer(participants_repository)
    
    response = controller.confirm(participant_id)
    
    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route('/trips/<trip_id>/activities', methods=['POST'])
def create_activity(trip_id):
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    controller = ActivityCreator(activities_repository)
    
    response = controller.create(request.json, trip_id)
    
    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route('/trips/<trip_id>/activities', methods=['GET'])
def get_activities(trip_id):
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    controller = ActivityFinder(activities_repository)
    
    response = controller.find_activities_from_trip(trip_id)
    
    return jsonify(response['body']), response['status_code']
