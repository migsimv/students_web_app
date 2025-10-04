from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return f"<Student {self.id} {self.first_name} {self.last_name}>"
