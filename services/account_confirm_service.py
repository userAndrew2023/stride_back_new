class BaseConfirmService:
    def __init__(self, user):
        self.user = user

    def sendConfirmationCode(self):
        pass

    def checkConfirmationCode(self):
        pass


class EmailConfirmService(BaseConfirmService):
    def sendConfirmationCode(self):
        pass

    def checkConfirmationCode(self):
        pass
