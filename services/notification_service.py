import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from models.notification import Notification
import smtplib

from models.user import User


class BaseNotificationService:
    def send_notification(self, notification: Notification):
        pass


class EmailNotificationService(BaseNotificationService):
    def __init__(self):
        self.smtpHost = "smtp.yandex.ru"
        self.smtpPort = 465
        self.sender_email = "alexseypw@yandex.ru"
        self.password = "lcbllimcnoduhzlt"

    def send_notification(self, notification: Notification):
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(self.smtpHost, self.smtpPort, context=context) as server:
            server.login(self.sender_email, self.password)
            for user in User.query.all():
                message = MIMEMultipart()
                message["From"] = self.sender_email
                message["To"] = user.email
                message["Subject"] = notification.header
                message.attach(MIMEText(notification.text, "plain"))
                server.sendmail(self.sender_email, user.email, message.as_string())
