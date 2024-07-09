from flask import Flask, Blueprint
from src.main.routes.trips_routes import trips_routes_bp

# Server config
app = Flask(__name__)

app.register_blueprint(trips_routes_bp)
