from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ModelExample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    col_example = db.Column(db.String(10))