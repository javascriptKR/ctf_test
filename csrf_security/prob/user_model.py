from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'   #테이블 이름 : users

    id = db.Column(db.Integer, primary_key = True)   #id를 프라이머리키로 설정
    userid = db.Column(db.String(32))
    username = db.Column(db.String(8))
    password = db.Column(db.String(64))