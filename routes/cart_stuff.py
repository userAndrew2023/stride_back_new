from flask import Blueprint, request, jsonify
from models import db
from models.cart_stuff import CartStuff
from models.product import Product

cartStuffBlueprint = Blueprint('cart_stuff', __name__, url_prefix='/cart-stuff')


@cartStuffBlueprint.route('/', methods=['GET'])
def get_cart_stuff():
    cart_stuff = CartStuff.query.all()
    response = []
    for i in cart_stuff:
        json_cart_stuff = i.to_dict()
        product = Product.query.get(i.product_id)
        if not product.in_store:
            delete_cart_stuff(i.id)
            continue
        json_cart_stuff['product'] = product.to_dict()
        response.append(json_cart_stuff)
    return jsonify({'cart_stuff': response})


@cartStuffBlueprint.route('/<int:cart_stuff_id>', methods=['GET'])
def get_cart_stuff_by_id(cart_stuff_id):
    cart_stuff = CartStuff.query.get_or_404(cart_stuff_id)
    return jsonify(cart_stuff.to_dict())


@cartStuffBlueprint.route('/', methods=['POST'])
def add_cart_stuff():
    data = request.get_json()
    new_cart_stuff = CartStuff(**data)
    new_cart_stuff.quantity = 1
    product: Product = Product.query.get(new_cart_stuff.product_id)
    if product.in_store:
        db.session.add(new_cart_stuff)
        db.session.commit()
    return jsonify({'stuff_id': new_cart_stuff.id})


@cartStuffBlueprint.route('/<int:cart_stuff_id>', methods=['PUT'])
def update_cart_stuff(cart_stuff_id):
    cart_stuff: CartStuff = CartStuff.query.get_or_404(cart_stuff_id)
    data = request.get_json()
    cart_stuff.quantity = data['quantity']
    if cart_stuff.quantity == 0:
        delete_cart_stuff(cart_stuff.id)
    db.session.commit()
    return jsonify({'message': 'Cart stuff updated successfully!'})


@cartStuffBlueprint.route('/<int:cart_stuff_id>', methods=['DELETE'])
def delete_cart_stuff(cart_stuff_id):
    db.session.delete(CartStuff.query.get_or_404(cart_stuff_id))
    db.session.commit()
    return jsonify({'message': 'Cart stuff deleted successfully!'})
