from server import db
from datetime import datetime

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), unique=True)
    title = db.Column(db.String(100), unique=True)
    date_added = db.Column(db.DateTime(), default=datetime.utcnow)

    def __init__(self, uri, title, date_added):
        self.url = uri
        self.title = title.lower()
        self.date_added = date_added
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Data {self.id} - {self.title}'