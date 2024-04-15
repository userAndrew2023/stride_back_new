from flask import Blueprint, request, jsonify
from models import db
from models.brand import Brand

brandsBlueprint = Blueprint('brands', __name__, url_prefix='/brands')


@brandsBlueprint.route('/', methods=['GET'])
def get_brands():
    return jsonify({'brands': Brand.query.all()})


@brandsBlueprint.route('/<int:brand_id>', methods=['GET'])
def get_brand(brand_id):
    return jsonify(Brand.query.get_or_404(brand_id))


@brandsBlueprint.route('/', methods=['POST'])
def add_brand():
    data = request.get_json()
    brand = Brand(**data)
    db.session.add(brand)
    db.session.commit()
    return jsonify({'message': 'Brand added successfully!'})


@brandsBlueprint.route('/<int:brand_id>', methods=['PUT'])
def update_brand(brand_id):
    Brand.query.get_or_404(brand_id)
    data = request.get_json()
    brand = Brand(**data)
    db.session.merge(brand)
    db.session.commit()
    return jsonify({'message': brand})


@brandsBlueprint.route('/<int:brand_id>', methods=['DELETE'])
def delete_brand(brand_id):
    db.session.delete(Brand.query.get_or_404(brand_id))
    db.session.commit()
    return jsonify({'message': 'Brand deleted successfully!'})
