from flask import Blueprint, request, jsonify
from models import db
from models.notification import Notification
from services.notification_service import EmailNotificationService

notificationsBlueprint = Blueprint('notifications', __name__, url_prefix='/notifications')


@notificationsBlueprint.route('/', methods=['GET'])
def get_notifications():
    return jsonify({'notifications': Notification.query.all()})


@notificationsBlueprint.route('/', methods=['POST'])
def add_notification():
    data = request.get_json()
    new_notification = Notification(**data)
    db.session.add(new_notification)
    db.session.commit()

    match new_notification.type:
        case 'email':
            service = EmailNotificationService(new_notification)
            service.send_notification()

    return jsonify({'message': 'Notification added successfully!'})
