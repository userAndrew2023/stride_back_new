import datetime

from sqlalchemy_serializer import SerializerMixin

from models import db


class PromoCode(db.Model, SerializerMixin):
    __tablename__ = 'promo_codes'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    percent = db.Column(db.Integer, nullable=False)
    active_from = db.Column(db.DateTime, default=datetime.datetime.now())
    active_to = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now(),
                           onupdate=datetime.datetime.now())
