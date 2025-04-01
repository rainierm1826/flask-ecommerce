from flask import Blueprint, jsonify, request
from app.models.product_model import Product
from app import db


product_bp = Blueprint('product', __name__)


@product_bp.route(rule="/create-product", methods=["POST"])
def create_product():
    try:
        data = request.json
        
        allowed_fields = {"product_name", "product_price", "product_stock", "product_image"}
        filtered_data = {key: value for key, value in data.items() if key in allowed_fields}
        
        new_product = Product(**filtered_data)
        db.session.add(new_product)
        db.session.commit()
        
        return jsonify(new_product.to_dict())
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@product_bp.route("/get-products", methods=["GET"])
def get_products():
    try:
        products = Product.query.all()
        return jsonify({"product": [product.to_dict() for product in products]}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@product_bp.route(rule="/get-product/<string:pid>", methods=["GET"])
def get_product(pid):
    try:
        product = Product.query.get(pid)
        
        if not product:
            return jsonify({"message": "product not found"})
        
        return jsonify(product.to_dict())
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@product_bp.route(rule="update-product/<string:pid>", methods=["PUT"])
def update_product(pid):
    try:
        
        data = request.get_json()
        
        if not pid:
            return jsonify({"message": "product not found"}), 404
        
        
        allowed_fields = {"product_name", "product_price", "product_stock", "product_image"}
        filtered_data = {key: value for key, value in data.items() if key in allowed_fields}
        
        result = Product.query.filter_by(pid=pid).update(filtered_data)
        
        db.session.commit()
        
        if result == 0:
            return jsonify({"message": "product not found"}), 404

        updated_product = Product.query.get(pid)
        return jsonify({"message": "User updated successfully", "product": updated_product.to_dict()}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@product_bp.route(rule="/delete-product/<string:pid>", methods=["DELETE"])
def delete_product(pid):
    try:
        product = Product.query.get(pid)
        
        if not product:
            return jsonify({"message": "product not found"}), 404
        
        db.session.delete(product)
        db.session.commit()
        
        return jsonify({"message": "product deleted successfully"}), 201
        
        
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500