from app import db
import uuid
from datetime import datetime
from sqlalchemy import func


class Product(db.Model):
    pid = db.Column(db.String(36), primary_key=True, default=lambda : str(uuid.uuid4()))
    product_name = db.Column(db.String(255))
    product_image = db.Column(db.Text)
    product_price = db.Column(db.Integer)
    product_stock = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())
    
    def to_dict(self):
        return {
            "pid": self.pid,
            "product_name": self.product_name,
            "product_image": self.product_image,
            "product_price" : self.product_price,
            "product_stock": self.product_stock,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
    