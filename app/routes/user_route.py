from flask import request, jsonify, Blueprint
from app import db
from app.models.user_model import User


main = Blueprint('main', __name__)

@main.route(rule="/", methods=["GET"])
def index():
    return "Hello"


# create user
@main.route(rule="/create-user", methods=["POST"])
def create_user():
    try:
        data = request.json
        
        user = User.query.filter_by(email=data["email"]).first()
        if user:
            return jsonify({"message": "user already exist"}), 409
        
        new_user = User(email=data["email"], first_name=data["first_name"], last_name=data["last_name"], age=data["age"])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "success"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

# get all users
@main.route(rule="/get-users", methods=["GET"])
def get_users():
    try:
        users = User.query.all()
        return jsonify({"users": [user.to_dict() for user in users]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# get user
@main.route(rule="/get-user/<int:uid>", methods=["GET"])
def get_user(uid):
    try:
        user = User.query.get(uid)
        
        if not user:
            return jsonify({"message": "user not found"}), 404
        
        return jsonify({"user": user.to_dict()})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# delete user
@main.route("/delete-user/<int:uid>", methods=["DELETE"])
def delete_user(uid):
    try:
        user = User.query.get(uid)

        if not user:
            return jsonify({"message": "user not found"}), 404

        db.session.delete(user)
        db.session.commit()

        return jsonify({"message": "user deleted"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# update user
@main.route(rule="/update-user/<int:uid>", methods=["PUT"])
def update_user(uid):
    try:
        user = User.query.get(uid)
        
        if not user:
            return jsonify({"message": "user not found"}), 404
        
        updated_user = request.json
        
        user.email = updated_user.get("email", user.email)
        user.first_name = updated_user.get("first_name", user.first_name)
        user.last_name = updated_user.get("last_name", user.last_name)
        user.age = updated_user.get("age", user.age)
        
        db.session.commit()
        
        return jsonify({"message": "updated successfully"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500