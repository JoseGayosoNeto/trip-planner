import os
from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from src.main.routes.trips_routes import trips_routes_bp
from src.main.routes.user_routes import user_routes_bp
from src.main.routes.token_routes import token_refresh_bp


load_dotenv(f'{os.path.abspath('.env')}')

# Server config
app = Flask(__name__)
jwt = JWTManager(app)

app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

app.register_blueprint(trips_routes_bp)
app.register_blueprint(user_routes_bp)
app.register_blueprint(token_refresh_bp)
