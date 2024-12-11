from flask import Flask, request, jsonify
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


    # CRUD routes
    @app.route('/')
    def index():
        return {"message": "Welcome to the app!"}


    # BIOLOGY
    # 'GET' all
    @app.route('/biologies', methods=['GET'])
    def all_biologies():
        try:
            biologies = Biology.query.all()
            return jsonify([biology.to_dict() for biology in biologies]), 200
        except ValueError as e:
            return jsonify({'errors': [str(e)]}), 400

    # 'GET' by id
    @app.route('/biologies/<int:id>', methods=['GET'])
    def biology_by_id(id):
        biology = Biology.query.filter_by(id=id).first()
        if not biology:
            return jsonify({'error': 'Biology not found'}), 404
        return jsonify(biology.to_dict()), 200

   
   # CORE
    # 'GET' all
    @app.route('/cores', methods=['GET'])
    def all_cores():
        try:
            cores = Core.query.all()
            return jsonify([core.to_dict() for core in cores]), 200
        except Exception as e:
            return jsonify({'errors': [str(e)]}), 500

    # 'GET' by id
    @app.route('/cores/<int:id>', methods=['GET'])
    def core_by_id(id):
        core = Core.query.filter_by(id=id).first()
        if not core:
            return jsonify({'error': 'Core emotion not found'}), 404
        return jsonify(core.to_dict()), 200

    # DIARY
        # 'GET' and 'POST' all
        # 'GET' by id

    # MIDDLE
        # 'GET' all
    @app.route('/middles', methods=['GET'])
    def all_middles():
        try:
            middles = Middle.query.all()
            return jsonify([middle.to_dict() for middle in middles]), 200
        except Exception as e:
            return jsonify({'errors': [str(e)]}), 500

    # 'GET' by id
    @app.route('/middles/<int:id>', methods=['GET'])
    def middle_by_id(id):
        middle = Middle.query.filter_by(id=id).first()
        if not middle:
            return jsonify({'error': 'Middle emotion not found'}), 404
        return jsonify(core.to_dict()), 200

    # OUTER
        # 'GET' all
    @app.route('/outers', methods=['GET'])
    def all_outers():
        try:
            outers = Outer.query.all()
            return jsonify([outer.to_dict() for outer in outers]), 200
        except Exception as e:
            return jsonify({'errors': [str(e)]}), 500
        # 'GET' by id
    @app.route('/outers/<int:id>', methods=['GET'])
    def outer_by_id(id):
        try:
            outer = Outer.query.get(id)
            if not outer:
                return jsonify({'error': 'Outer emotion not found'}), 404
            return jsonify(outer.to_dict()), 200
        except Exception as e:
            return jsonify({'errors': [str(e)]}), 500

    # PHYSIOLOGY
        # 'GET' all
        # 'GET' by id

    # USER
        # 'GET' and 'POST' all
        # 'GET' and 'DELETE' by id

    # VULNERABILITY
        # 'GET' all
        # 'GET' by id

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5555, debug=True)