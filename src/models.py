from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TrackingData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.JSON)
    created = db.Column(db.DateTime, default=datetime.now)
