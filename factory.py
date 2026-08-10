class Notification:
    def send(self):
        pass


class EmailNotification(Notification):
    def send(self):
        print("Sending Email")


class SMSNotification(Notification):
    def send(self):
        print("Sending SMS")


class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        if notification_type == "email":
            return EmailNotification()

        if notification_type == "sms":
            return SMSNotification()

        raise ValueError("Invalid notification type")
    

# usage
notification = NotificationFactory.create_notification("email")

notification.send()

# without

# notification_type = "email"

# if notification_type == "email":
#     notification = EmailNotification()
# elif notification_type == "sms":
#     notification = SMSNotification()

# notification.send()