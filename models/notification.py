import datetime

from sqlalchemy_serializer import SerializerMixin

from models import db


class Notification(db.Model, SerializerMixin):
    __tablename__ = 'notification'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Text, nullable=False)
    header = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now(),
                           onupdate=datetime.datetime.now())
