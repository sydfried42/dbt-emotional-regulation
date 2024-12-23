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
    # 'GET' all
    @app.route('/diaries', methods=['GET'])
    def all_diaries():
        diaries = Diary.query.all()
        return [diary.to_dict() for diary in diaries], 200


    # 'GET' by id
    @app.route('/diaries/<int:id>', methods=['GET'])
    def diary_by_id(id):
        diary = Diary.query.filter(Diary.id == id).first()
        if not diary:
            return {'error': 'diary entry not found'}, 404
        return diary.to_dict(), 200


    # 'POST'
    @app.route('/diaries', methods=['POST'])
    def create_diary():
        json_data = request.get_json()

        try:
            new_diary = Diary(
                title=json_data.get('title'),
                content=json_data.get('content'),
                user_id=json_data.get('user_id'),
                date=json_data.get('date')
            )
        except ValueError as e:
            return {'errors': [str(e)]}, 400

        db.session.add(new_diary)
        db.session.commit()
        return new_diary.to_dict(), 201



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
    @app.route('/physiologies', methods=['GET'])
    def all_physiologies():
        try:
            physiologies = Physiology.query.all()
            return jsonify([physiology.to_dict() for physiology in physiologies]), 200
        except Exception as e:
            return jsonify({'errors': [str(e)]}), 500
    # 'GET' by id
    @app.route('/physiologies/<int:id>', methods=['GET'])
    def physiology_by_id(id):
        try:
            physiology = Physiology.query.get(id)
            if not physiology:
                return jsonify({'error': 'Physiology not found'}), 404
            return jsonify(physiology.to_dict()), 200
        except Exception as e:
            return jsonify({'errors': [str(e)]}), 500


    # USER
    # 'GET' all
    @app.route('/users', methods=['GET'])
    def all_users():
        users = User.query.all()
        return [user.to_dict() for user in users], 200


    # 'POST'
    @app.route('/users', methods=['POST'])
    def create_user():
        json_data = request.get_json()

        try:
            new_user = User(
                username=json_data.get('username'),
                email=json_data.get('email'),
                password=json_data.get('password'),  # Assumed you handle password securely elsewhere
                first_name=json_data.get('first_name'),
                last_name=json_data.get('last_name')
            )
        except ValueError as e:
            return {'errors': [str(e)]}, 400

        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict(), 201


    # 'GET' by id
    @app.route('/users/<int:id>', methods=['GET'])
    def user_by_id(id):
        user = User.query.filter(User.id == id).first()
        if not user:
            return {'error': 'user not found'}, 404
        return user.to_dict(), 200


    # 'DELETE' by id
    @app.route('/users/<int:id>', methods=['DELETE'])
    def delete_user(id):
        user = User.query.filter(User.id == id).first()
        if not user:
            return {'error': 'user not found'}, 404

        db.session.delete(user)
        db.session.commit()
        return {}, 204



    # VULNERABILITY
    # 'GET' all
    @app.route('/vulnerabilities', methods=['GET'])
    def all_vulnerabilities():
        try:
            vulnerabilities = Vulnerability.query.all()
            return jsonify([vulnerability.to_dict() for vulnerability in vulnerabilities]), 200
        except Exception as e:
            return jsonify({'errors': [str(e)]}), 500
    # 'GET' by id
    @app.route('/vulnerabilities/<int:id>', methods=['GET'])
    def vulnerability_by_id(id):
        try:
            vulnerability = Vulnerability.query.get(id)
            if not vulnerability:
                return jsonify({'error': 'Vulnerability not found'}), 404
            return jsonify(vulnerability.to_dict()), 200
        except Exception as e:
            return jsonify({'errors': [str(e)]}), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5555, debug=True)