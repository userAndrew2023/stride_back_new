from flask import Blueprint, request, jsonify, abort
from models import db
from models.promo_code import PromoCode

promoCodesBlueprint = Blueprint('promo_codes', __name__, url_prefix='/promo-codes')


@promoCodesBlueprint.route('/', methods=['GET'])
def get_promo_codes():
    promo_codes = PromoCode.query.all()
    return jsonify({'promo_codes': [promo.to_dict() for promo in promo_codes]})


@promoCodesBlueprint.route('/<promoCode>', methods=['GET'])
def get_promo_code(promoCode):
    promo_code = PromoCode.query.where(PromoCode.name == promoCode).first()
    if promo_code is not None:
        return jsonify(promo_code.to_dict())
    return jsonify({'msg': 'not found'})


@promoCodesBlueprint.route('/', methods=['POST'])
def add_promo_code():
    data = request.get_json()
    new_promo_code = PromoCode(**data)
    db.session.add(new_promo_code)
    db.session.commit()
    return jsonify({'message': 'Promo code added successfully!'})


@promoCodesBlueprint.route('/<int:promo_code_id>', methods=['PUT'])
def update_promo_code(promo_code_id):
    promo_code = PromoCode.query.get_or_404(promo_code_id)
    data = request.get_json()
    promo_code.update(data)  # Assuming PromoCode has an update method
    db.session.commit()
    return jsonify({'message': 'Promo code updated successfully!'})


@promoCodesBlueprint.route('/<int:promo_code_id>', methods=['DELETE'])
def delete_promo_code(promo_code_id):
    db.session.delete(PromoCode.query.get_or_404(promo_code_id))
    db.session.commit()
    return jsonify({'message': 'Promo code deleted successfully!'})
