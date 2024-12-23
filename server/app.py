from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# Import the db instance from models
from models import db, User, Diary, Vulnerability, Biology, Physiology, Core, Middle, Outer

# Common helper function to handle fetching by ID
def get_by_id(model, id, error_message):
    record = model.query.filter_by(id=id).first()
    if not record:
        return jsonify({'error': error_message}), 404
    return jsonify(record.to_dict()), 200

# CRUD route helper function for `GET all` requests
def get_all(model):
    try:
        records = model.query.all()
        return jsonify([record.to_dict() for record in records]), 200
    except Exception as e:
        return jsonify({'errors': [str(e)]}), 500

# Function to create an entry
def create_entry(model, data):
    try:
        new_entry = model(**data)
    except ValueError as e:
        return jsonify({'errors': [str(e)]}), 400
    db.session.add(new_entry)
    db.session.commit()
    return jsonify(new_entry.to_dict()), 201

def create_app():
    # Create a Flask application object
    app = Flask(__name__)

    # Initialize CORS
    CORS(app)

    # Configure a database connection
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.json.compact = False

    # Initialize the database with the Flask app
    db.init_app(app)

    # Create a Migrate object to manage schema modifications
    migrate = Migrate(app, db)

    @app.route('/')
    def index():
        return {"message": "Welcome to the app!"}

    # BIOLOGY
    @app.route('/biologies', methods=['GET'])
    def all_biologies():
        return get_all(Biology)

    @app.route('/biologies/<int:id>', methods=['GET'])
    def biology_by_id(id):
        return get_by_id(Biology, id, 'Biology not found')

    # CORE
    @app.route('/cores', methods=['GET'])
    def all_cores():
        return get_all(Core)

    @app.route('/cores/<int:id>', methods=['GET'])
    def core_by_id(id):
        return get_by_id(Core, id, 'Core emotion not found')

    # DIARY
    @app.route('/diaries', methods=['GET'])
    def all_diaries():
        return get_all(Diary)

    @app.route('/diaries/<int:id>', methods=['GET'])
    def diary_by_id(id):
        return get_by_id(Diary, id, 'Diary entry not found')

    @app.route('/diaries', methods=['POST'])
    def create_diary():
        json_data = request.get_json()
        data = {
            'title': json_data.get('title'),
            'content': json_data.get('content'),
            'user_id': json_data.get('user_id'),
            'date': json_data.get('date')
        }
        return create_entry(Diary, data)

    # MIDDLE
    @app.route('/middles', methods=['GET'])
    def all_middles():
        return get_all(Middle)

    @app.route('/middles/<int:id>', methods=['GET'])
    def middle_by_id(id):
        return get_by_id(Middle, id, 'Middle emotion not found')

    # OUTER
    @app.route('/outers', methods=['GET'])
    def all_outers():
        return get_all(Outer)

    @app.route('/outers/<int:id>', methods=['GET'])
    def outer_by_id(id):
        return get_by_id(Outer, id, 'Outer emotion not found')

    # PHYSIOLOGY
    @app.route('/physiologies', methods=['GET'])
    def all_physiologies():
        return get_all(Physiology)

    @app.route('/physiologies/<int:id>', methods=['GET'])
    def physiology_by_id(id):
        return get_by_id(Physiology, id, 'Physiology not found')

    # USER
    @app.route('/users', methods=['GET'])
    def all_users():
        return get_all(User)

    @app.route('/users', methods=['POST'])
    def create_user():
        json_data = request.get_json()
        data = {
            'username': json_data.get('username'),
            'email': json_data.get('email'),
            'password': json_data.get('password'),
            'first_name': json_data.get('first_name'),
            'last_name': json_data.get('last_name')
        }
        return create_entry(User, data)

    @app.route('/users/<int:id>', methods=['GET'])
    def user_by_id(id):
        return get_by_id(User, id, 'User not found')

    @app.route('/users/<int:id>', methods=['DELETE'])
    def delete_user(id):
        user = User.query.filter(User.id == id).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404
        db.session.delete(user)
        db.session.commit()
        return jsonify({}), 204

    # VULNERABILITY
    @app.route('/vulnerabilities', methods=['GET'])
    def all_vulnerabilities():
        return get_all(Vulnerability)

    @app.route('/vulnerabilities/<int:id>', methods=['GET'])
    def vulnerability_by_id(id):
        return get_by_id(Vulnerability, id, 'Vulnerability not found')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5555, debug=True)
