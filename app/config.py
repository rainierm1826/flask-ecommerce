import os
from dotenv import load_dotenv
from flask import Flask


load_dotenv()

app = Flask(__name__)

class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('USER')}:{os.getenv('PASSWORD')}@localhost:{os.getenv('PORT')}/{os.getenv('DATABASE')}"
    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False