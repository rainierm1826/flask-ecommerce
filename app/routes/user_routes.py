from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.user_model import User
from flask_jwt_extended import create_access_token
from datetime import timedelta

user_bp = Blueprint('user', __name__)


@user_bp.route(rule="/sign-up", methods=["POST"])
def create_user():
    try:
        data = request.json
        user = User.query.filter_by(email=data["email"]).first()
        
        if user:
            return jsonify({"message": "email already exist"}), 409
        
        new_user = User(
            email=data["email"],
            password=User.hash_password(data["password"]),
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({"message": "success"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@user_bp.route(rule="/sign-in", methods=["POST"])
def sign_in():
    try:
        data = request.json
        
        user = User.query.filter_by(email=data["email"]).first()
        
        if not user or not user.check_password(password=data["password"]):
            return jsonify({"message": "Invalid email or password"}), 401
        
        access_token = create_access_token(identity=user.uid)
        response = make_response(jsonify({"message": "login successfully"}))
        response.set_cookie("access_token", access_token, httponly=False, secure=False, samesite="Strict")
        return response
    
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
    

@user_bp.route(rule="/update-user", methods=["PUT"])
def update_user():
    try:
        data = request.get_json()
        uid = data.get("uid")

        if not uid:
            return jsonify({"message": "User ID is required"}), 400

        allowed_fields = {"email", "password", "first_name", "last_name", "middle_name"}
        filtered_data = {key: value for key, value in data.items() if key in allowed_fields}

        if not filtered_data:
            return jsonify({"message": "No valid fields provided for update"}), 400

        result = User.query.filter_by(uid=uid).update(filtered_data)

        if result == 0:
            return jsonify({"message": "User not found"}), 404

        db.session.commit()

        updated_user = User.query.get(uid)
        return jsonify({"message": "User updated successfully", "user": updated_user.to_dict()}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
