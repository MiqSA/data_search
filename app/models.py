from server import db
from datetime import datetime


def default_return(data):
    if data:
        if len(data)>1:
            res = []
            for d in data:
                partial =  {'id': d[0], 'url': d[1], 'title': d[2], 'date_added':d[3]}
                res.append(partial)
            return res
        return [{'id': data[0], 'url': data[1], 'title': data[2], 'date_added':data[3]}]
    return None

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), unique=True)
    title = db.Column(db.String(100), unique=True)
    date_added = db.Column(db.DateTime(), default=datetime.utcnow)

    def __init__(self, uri=None, title=None, date_added=None):
        self.url = uri
        self.title = title
        self.date_added = date_added

    @classmethod
    def find_by_date_after(cls, start_date):
        try:
            data = db.session.query(
                cls.id,
                cls.url,
                cls.title,
                cls.date_added).filter(cls.date_added > start_date).all()
            return default_return(data)
        except Exception as err:

            print('Error in find by date after', err)
            return None

    @classmethod
    def find_by_date_before(cls, end_date):
        try:
            data = db.session.query(
                cls.id,
                cls.url,
                cls.title,
                cls.date_added).filter(cls.date_added < end_date).all()
            return default_return(data)
        except Exception as err: 
            print('Error in find by date before', err)
            return None

    @classmethod
    def find_by_date_between(cls, start_date, end_date):
        try:
            data = db.session.query(
                cls.id,
                cls.url,
                cls.title,
                cls.date_added).filter(cls.date_added.between(start_date, end_date)).all()
            return default_return(data)
        except Exception as err:
            print('Error in find by date between', err)
            return None

    @classmethod
    def find_by_title(cls, title):
        try:
            data = db.session.query(
                cls.id,
                cls.url,
                cls.title,
                cls.date_added).filter(
                    cls.title.like(f'%{title}%')
                    ).all()
            return default_return(data)
        except Exception as err:
            print('Error in find by title', err)
            return None

    @classmethod
    def find_by_uri(cls, uri):
        try:
            data = db.session.query(
                cls.id,
                cls.url,
                cls.title,
                cls.date_added).filter(
                    cls.url.like(f'%{uri}%')
                    ).all()
            return default_return(data)
        except Exception as err:
            print('Error in find by uri', err)
            return None
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Data {self.id} - {self.title}'