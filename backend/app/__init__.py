from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .config import Config
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    
    CORS(app, origins=["http://localhost:3000"], supports_credentials=True)

    from .routes.user_routes import user_bp
    from .routes.product_routes import product_bp
    from .routes.order_routes import order_bp
    
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(product_bp, url_prefix="/product")
    app.register_blueprint(order_bp, url_prefix="/order")

    return app
