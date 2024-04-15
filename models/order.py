import datetime

from sqlalchemy_serializer import SerializerMixin

from models import db


class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    payment_status = db.Column(db.Boolean, default=False)
    delivery_address = db.Column(db.Text, nullable=False)
    comment = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now(),
                           onupdate=datetime.datetime.now())
