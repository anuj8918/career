from flask import Blueprint, jsonify

recommendations_bp = Blueprint('recommendations', __name__)

@recommendations_bp.route('/recommendations/<int:user_id>', methods=['GET'])
def get_recommendations(user_id):
    # In real implementation, you'd use a trained ML model for recommendations
    recommendations = ["Software Engineer", "Data Scientist", "Product Manager"]
    return jsonify({
        "user_id": user_id,
        "recommendations": recommendations
    })
