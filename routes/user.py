from flask import Blueprint, request, jsonify
from models import db
from models.user import User

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/register', methods=['POST'])
def register():
    data = request.json()
    email = data.get('email')
    name = data.get('name')
    surname = data.get('surname')
    phone = data.get('phone')
    password = data.get('password')

    user = User(email=email, name=name, surname=surname, phone=phone)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Missing email or password'}), 400

    user = User.query.filter_by(email=email).first()

    if user is None or not user.check_password(password):
        return jsonify({'error': 'Invalid email or password'}), 401

    return jsonify({'message': 'Login successful'}), 200


@user_bp.route('/logout', methods=['POST'])
def logout():
    return jsonify({'message': 'Logout successful'}), 200
