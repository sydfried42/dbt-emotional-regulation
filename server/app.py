from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# Import the db instance from models
from models import db, User, Diary, Vulnerability, Biology, Physiology, Core, Middle, Outer

def create_app():
    # Create a Flask application object
    app = Flask(__name__)

    # Initialize CORS
    CORS(app)

    # Configure a database connection to the local file app.db
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.json.compact = False

    # Initialize the database with the Flask app
    db.init_app(app)

    # Create a Migrate object to manage schema modifications
    migrate = Migrate(app, db)

    # Create database tables (for initial setup only)
    with app.app_context():
        db.create_all()  # Remove this if you're using migrations to create tables

    # CRUD routes (add your routes here)
    @app.route('/')
    def index():
        return {"message": "Welcome to the app!"}

    # Add more routes as needed...

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5555, debug=True)