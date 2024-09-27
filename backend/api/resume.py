from flask import Blueprint, request, jsonify
from models.resume_model import Resume
from models.user_model import User
from database import db

resume_bp = Blueprint('resume', __name__)

@resume_bp.route('/resume/<int:user_id>', methods=['POST'])
def create_resume(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    
    data = request.json
    resume = Resume(
        user_id=user.id,
        summary=data.get('summary'),
        education=data.get('education'),
        experience=data.get('experience'),
        skills=data.get('skills')
    )
    db.session.add(resume)
    db.session.commit()
    return jsonify({"message": "Resume created successfully"}), 201

@resume_bp.route('/resume/<int:user_id>', methods=['GET'])
def get_resume(user_id):
    resumes = Resume.query.filter_by(user_id=user_id).all()
    if not resumes:
        return jsonify({"message": "No resumes found for this user."}), 404
    
    resume_data = []
    for resume in resumes:
        resume_data.append({
            "id": resume.id,
            "summary": resume.summary,
            "education": resume.education,
            "experience": resume.experience,
            "skills": resume.skills
        })
    return jsonify(resume_data), 200
