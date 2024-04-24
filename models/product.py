import datetime
from app import db
from sqlalchemy_serializer import SerializerMixin


class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    old_price = db.Column(db.Float, nullable=False)
    in_store = db.Column(db.Boolean, default=False)
    available = db.Column(db.Integer, default=0)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now(),
                           onupdate=datetime.datetime.now())
