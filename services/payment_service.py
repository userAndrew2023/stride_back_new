import uuid

import requests

from models import db
from models.order import Order
from models.order_stuff import OrderStuff


class BasePaymentService:
    def issueInvoice(self, quantity, order):
        pass

    def checkInvoice(self, body):
        pass


class YookassaPaymentStatuses:
    EVENT_PAYMENT_SUCCEEDED = 'payment.succeeded'
    EVENT_PAYMENT_WAITING = 'payment.waiting_for_capture'
    EVENT_PAYMENT_CANCELED = 'payment.canceled'
    EVENT_REFUND_SUCCEEDED = 'refund.succeeded'


class YookassaPaymentService(BasePaymentService):
    def __init__(self):
        self.shopId = '320062'
        self.apiKey = 'test_Vfi3MBZSbXFSRm74KvDf2bN8mwLMW_ctUhEpmBMy_zI'

    def issueInvoice(self, quantity, order):
        headers = {
            'Idempotence-Key': str(uuid.uuid4()),
            'Content-Type': 'application/json',
        }

        json_data = {
            'amount': {
                'value': quantity,
                'currency': 'RUB',
            },
            'capture': True,
            'confirmation': {
                'type': 'redirect',
                'return_url': 'http://192.168.0.102:8080/',
            },
            'description': f'Заказ #{order.id}',
        }

        response = requests.post('https://api.yookassa.ru/v3/payments', headers=headers, json=json_data,
                                 auth=(self.shopId, self.apiKey))
        return response.json()

    def checkInvoice(self, body: dict):
        event = body['event']
        match event:
            case YookassaPaymentStatuses.EVENT_PAYMENT_SUCCEEDED:
                order_id = body['object']['description'].split("#")[1]
                order: Order = Order.query.get(order_id)
                order.payment_status = True
                for i in OrderStuff.query.where(OrderStuff.order_id == order.id):
                    i.status = 'confirm'
                db.session.commit()
