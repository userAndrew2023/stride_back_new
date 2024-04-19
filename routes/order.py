from flask import Blueprint, request, jsonify
from models import db
from models.cart_stuff import CartStuff
from models.order import Order
from models.order_stuff import OrderStuff
from models.product import Product
from models.promo_code import PromoCode
from models.user import User

ordersBlueprint = Blueprint('orders', __name__, url_prefix='/orders')


@ordersBlueprint.route('/', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify({'orders': [order.to_dict() for order in orders]})


@ordersBlueprint.route('/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get_or_404(order_id)
    return jsonify(order.to_dict())


def subtract_percent(number, percent):
    print(number, number - (number * percent / 100))
    return number - (number * percent / 100)


@ordersBlueprint.route('/', methods=['POST'])
def add_order():
    data: dict = request.get_json()
    stuff: list = data.pop("stuff")
    promo_code = None
    if data.get('promo_code'):
        promo_code = data.pop("promo_code")
    new_order = Order(**data)
    new_order.payment_status = False
    db.session.add(new_order)
    for i in stuff:
        new_stuff = OrderStuff(**i)
        CartStuff.query.where(CartStuff.product_id == new_stuff.product_id).where(CartStuff.user_id == 1).delete()
        product = Product.query.get(new_stuff.product_id)
        if product.available > 0:
            product.available -= 1

        new_stuff.order_id = new_order.id
        new_stuff.price = product.sale_price
        if promo_code:
            new_stuff.price = subtract_percent(new_stuff.price, PromoCode.query.where(PromoCode.name == promo_code).first().percent)
        new_stuff.name = product.name
        db.session.add(new_stuff)
    db.session.commit()

    return jsonify({
        'order': new_order.to_dict(),
        'stuff': [i.to_dict() for i in OrderStuff.query.where(OrderStuff.order_id == new_order.id).all()]
    })


@ordersBlueprint.route('/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    order = Order.query.get_or_404(order_id)
    data = request.get_json()
    order.update(data)
    db.session.commit()
    return jsonify({'message': 'Order updated successfully!'})


@ordersBlueprint.route('/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    db.session.delete(Order.query.get_or_404(order_id))
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully!'})
