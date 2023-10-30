from flask import (
    Blueprint,
    request,
    jsonify,
    session
)
from flask_jwt_extended import (
    create_access_token,
    jwt_required
)
from flask_cors import cross_origin
from app.models.user import User
from app import db

auth_bp = Blueprint("auth", __name__)


@auth_bp.route('/register', methods=['POST'])
@cross_origin()
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    if not username or not password or not email or not first_name or not last_name:
        return jsonify({'message': 'All fiels are required'}), 400

    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'message': 'Username already exists'}), 400

    if User.query.filter_by(email=email).first() is not None:
        return jsonify({'message': 'Email address already in use'}), 400

    user = User(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name
    )
    print(user)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 200


@auth_bp.route('/login', methods=['POST'])
@cross_origin()
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity=username)
        return jsonify({'access_token': access_token}), 200

    return jsonify({'message': 'Invalid username or password'}), 401
