from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

# Import Controllers/Services
from src.authentication.services.token_service import RefreshTokenService

# Import Repositories
from src.models.repositories.users_repository import UsersRepository

# Import Connection
from src.models.settings.db_connection_handler import db_connection_handler

token_refresh_bp = Blueprint("token_refresh", __name__)

@token_refresh_bp.route('/token/refresh', methods=['POST'])
@jwt_required(refresh=True)
def create_new_tokens():
    conn = db_connection_handler.get_connection()
    users_repository = UsersRepository(conn)
    service = RefreshTokenService(users_repository)
    
    response = service.create_new_valid_token()
    
    return jsonify(response['body']), response['status_code']
