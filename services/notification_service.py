from models.notification import Notification


class BaseNotificationService:
    def __init__(self, notification: Notification):
        self.notification: Notification = notification

    def send_notification(self):
        pass


class EmailNotificationService(BaseNotificationService):
    def send_notification(self):
        pass
