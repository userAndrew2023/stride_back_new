import datetime

from models import db
from sqlalchemy_serializer import SerializerMixin


class Brand(db.Model, SerializerMixin):
    __tablename__ = 'brands'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now(),
                           onupdate=datetime.datetime.now())
