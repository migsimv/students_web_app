from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    age = db.Column(db.Integer)                                
    birth_date = db.Column(db.Date)                             #
    active = db.Column(db.Boolean, default=True)     
