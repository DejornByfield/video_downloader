from .database import db
from datetime import datetime

class Download(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    title = db.Column(db.String(200), nullable=True)
    filepath = db.Column(db.String(500), nullable=True)
    filesize = db.Column(db.String(50), nullable=True)
    status = db.Column(db.String(20), nullable=False, default='completed')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)