from PersonalWeb import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id = db.Column(db.Integer ,primary_key = True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def set_password(self , password):
        self.password_hash = generate_password_hash(password)
    
    def validate_password(self ,password):
        return check_password_hash(self.password_hash,password)


class Message(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime , default = datetime.utcnow , index = True)

# utcnow 表示現在的世界協調時間
# 在這裡不要加括號 
# index = True 表示在這欄位加索引，這樣在搜索 timestamp 時會變快

class Story(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(20))
    body = db.Column(db.String(200))
    site = db.Column(db.String(255),default = '/story')

  