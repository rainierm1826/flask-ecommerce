from app import db
from uuid import uuid4
from datetime import datetime
from sqlalchemy import func

class Orders(db.Model):
    
    oid = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    uid = db.Column(db.String(36), db.ForeignKey("user.uid"), nullable=False)
    pid = db.Column(db.String(36), db.ForeignKey("product.pid"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())
    
    user = db.relationship("User", backref="orders")
    product = db.relationship("Product", backref="orders")
    
    def to_dict(self):
        return {
            "oid": self.oid,
            "user": {
                "uid": self.user.uid,
                "email": self.user.email,
                "first_name": self.user.first_name,
                "last_name": self.user.last_name,
                "middle_name": self.user.middle_name,
            },
            "product":{
              "pid": self.product.pid,
              "product_name": self.product.product_name,
              "product_price": self.product.product_price,
            },
            "quantity": self.quantity,
            "total_price": self.product.product_price * self.quantity,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }