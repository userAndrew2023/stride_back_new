from flask import Blueprint, request, jsonify
from models import db
from models.cart_stuff import CartStuff
from models.product import Product

productsBlueprint = Blueprint('products', __name__, url_prefix='/products')


@productsBlueprint.route('/', methods=['GET'])
def get_products():
    query = Product.query.where(Product.in_store)
    search = request.args.get('q')
    if search:
        for word in search.split():
            query = query.filter(Product.name.ilike(f"%{word}%"))
    response = {
        "products": []
    }
    for i in query.all():
        dict_product = i.to_dict()
        cartStuff = CartStuff.query.where(CartStuff.product_id == i.id).where(CartStuff.user_id == 1).first()
        if cartStuff:
            in_cart = cartStuff.quantity
            dict_product['cart_stuff_id'] = cartStuff.id
        else:
            in_cart = 0
        dict_product['in_cart'] = in_cart
        response["products"].append(dict_product)
    return jsonify({'data': response})


@productsBlueprint.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    return jsonify(Product.query.get_or_404(product_id).to_dict())


@productsBlueprint.route('/', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = Product(**data)
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully!'})


@productsBlueprint.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    Product.query.get_or_404(product_id)
    data = request.get_json()
    product = Product(**data)
    db.session.merge(product)
    db.session.commit()
    return jsonify({'message': 'Product updated successfully!'})


@productsBlueprint.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    db.session.delete(Product.query.get_or_404(product_id))
    for cart_stuff in CartStuff.query.filter_by(product_id=product_id).all():
        db.session.delete(cart_stuff)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully!'})
