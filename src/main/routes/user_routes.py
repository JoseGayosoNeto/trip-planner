from flask import Blueprint, request, jsonify

# Import Controllers/Services
from src.authentication.services.user_service import AuthenticationService
from src.controllers.user_creator import UserCreator

# Import Repositories
from src.models.repositories.users_repository import UsersRepository

# Import Connection
from src.models.settings.db_connection_handler import db_connection_handler


user_routes_bp = Blueprint('user_routes', __name__)

@user_routes_bp.route('/register', methods=['POST'])
def register_new_user():
    conn = db_connection_handler.get_connection()
    users_repository = UsersRepository(conn)
    controller = UserCreator(users_repository)
    
    response = controller.create(request.json)
    
    return jsonify(response['body']), response['status_code']

@user_routes_bp.route('/login', methods=['POST'])
def login():
    conn = db_connection_handler.get_connection()
    users_repository = UsersRepository(conn)
    service = AuthenticationService(users_repository)
    
    response = service.login(request.json)
    
    return jsonify(response['body']), response['status_code']
