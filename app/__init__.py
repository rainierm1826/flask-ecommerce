from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    db.init_app(app)
    
    # register blueprints
    from .routes.user_routes import user_bp
    from .routes.product_routes import product_bp
    from .routes.order_routes import order_bp
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(product_bp, url_prefix="/product")
    app.register_blueprint(order_bp, url_prefix="/order")
    
    return app