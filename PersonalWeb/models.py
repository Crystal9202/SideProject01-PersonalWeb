from PersonalWeb import db
from datetime import datetime

class Message(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime , default = datetime.utcnow , index = True)


class Story(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(20))
    body = db.Column(db.String(200))
    site = db.Column(db.String(255),default = '/story')