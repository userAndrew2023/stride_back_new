from flask import Blueprint, request, jsonify

from models.order import Order
from models.order_stuff import OrderStuff
from services.payment_service import YookassaPaymentService

paymentsBlueprint = Blueprint('payments', __name__, url_prefix='/payments')


@paymentsBlueprint.route('/', methods=['POST'])
def create_payment():
    payment = YookassaPaymentService()
    data: dict = request.get_json()

    order = Order.query.get(data.get('order_id'))
    quantity = sum(i.quantity * i.price for i in OrderStuff.query.where(OrderStuff.order_id == order.id).all())

    return jsonify(payment.issueInvoice(quantity, order))


@paymentsBlueprint.route('/success', methods=['POST'])
def successful_payment():
    payment = YookassaPaymentService()
    payment.checkInvoice(request.get_json())
    return jsonify({"status": "ok"}), 200
