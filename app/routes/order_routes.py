from flask import Blueprint, request, jsonify
from app.models.order_model import Orders
from app.models.product_model import Product
from app import db

order_bp = Blueprint('order', __name__)

@order_bp.route(rule="/create-order/<string:pid>", methods=["POST"])
def create_order(pid):
    try:
        
        data = request.json
        uid = data.get("uid")
        quantity = data.get("quantity")
        
        product = Product.query.get(pid)
        
        if product.product_stock < quantity:
            return jsonify({"message": f"we only have {product.product_stock}"}), 400
    
        with db.session.begin_nested():
            new_order = Orders(uid=uid, pid=pid, quantity=quantity)
            db.session.add(new_order)
            
            product.product_stock -= quantity
            db.session.add(product)
        
        db.session.commit()
        
        return jsonify({"message": "order successfully"})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    

@order_bp.route(rule="/get-orders", methods=["GET"])
def get_orders():
    try:
        orders = Orders.query.all()
        
        return jsonify({"orders": [order.to_dict() for order in orders]})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    