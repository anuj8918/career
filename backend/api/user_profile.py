from flask import Blueprint, request, jsonify
from models.user_model import User
from database import db

user_profile_bp = Blueprint('user_profile', __name__)

@user_profile_bp.route('/user', methods=['POST'])
def create_user():
    data = request.json
    user = User(
        name=data['name'],
        email=data['email'],
        skills=data.get('skills', []),
        interests=data.get('interests', []),
        personality_quiz_results=data.get('personality_quiz_results', {}),
        career_preferences=data.get('career_preferences', {})
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

@user_profile_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify({
        "name": user.name,
        "email": user.email,
        "skills": user.skills,
        "interests": user.interests
    })
