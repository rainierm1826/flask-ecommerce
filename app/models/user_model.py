from app import db

class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    
    def to_dict(self):
        return {
            "uid": self.uid,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
    
    def __repr__(self):
        return f"<User {self.email}, {self.first_name}, {self.last_name}, {self.age}>"