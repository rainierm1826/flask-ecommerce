from flask import Blueprint, request, jsonify
from app import db
from app.models.user_model import User

user_bp = Blueprint('user', __name__)


@user_bp.route(rule="/create-user", methods=["POST"])
def create_user():
    try:
        data = request.json
        
        user = User.query.filter_by(email=data["email"]).first()
        
        allowed_fields = {"email", "password", "first_name", "last_name", "middle_name"}
        filtered_data = {key: value for key, value in data.items() if key in allowed_fields}
        
        if user:
            return jsonify({"message": "email already exist"}), 409
        
        new_user = User(**filtered_data)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({"message": "success"}), 201
    
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@user_bp.route(rule="/get-users", methods=["GET"])
def get_users():
    try:
        users = User.query.all()
        return jsonify({"users": [user.to_dict() for user in users]}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@user_bp.route(rule="/get-user/<string:uid>", methods=["GET"])
def get_user(uid):
    try:
        user = User.query.filter_by(uid=uid).first()
        if not user:
            return jsonify({"message": "user not found"}), 409
        return jsonify(user.to_dict()), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500