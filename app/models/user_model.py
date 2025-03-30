from app import db
import uuid
from datetime import datetime
from sqlalchemy import func

class User(db.Model):
    uid = db.Column(db.String(36), primary_key=True, default=lambda : str(uuid.uuid4())) # this makes the id a random string
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    middle_name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())
    
    def to_dict(self):
        return {
            "uid": self.uid,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "middle_name": self.middle_name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
        
    