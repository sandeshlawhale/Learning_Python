class Notification:
    def send(self, message):
        if message == "":
            raise ValueError("Message should be something for notification")


class EmailNotification(Notification):
    def __init__(self, mail, sub, msg):
        self.email = mail
        self.subject = sub
        self.message = msg

    def send(self):
        super().send(self.message)

        return f"'{self.message}' send to you by {self.email}"


class SMSNotification(Notification):
    def __init__(self, phone, msg):
        self.phone = phone
        self.message = msg

    def send(self):
        super().send(self.message)

        return f"'{self.message}' send to you by {self.phone}"


class PushNotification(Notification):
    def __init__(self, name, msg):
        self.name = name
        self.message = msg

    def send(self):
        super().send(self.message)

        return f"'{self.message}' send to you by {self.name}"


notifications = [
    EmailNotification("janedoe@gmila.com", "test", "test mail"),
    SMSNotification("9988776655", "test msg"),
    PushNotification("John", "test msg"),
]

for notification in notifications:
    print(notification.send())
