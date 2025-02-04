from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass


class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Email notifier: {message}")


class SMSNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"SMS notifier: {message}")


class PushNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Push notifier: {message}")


class NotifierService(ABC):
    @abstractmethod
    def create_notifier(self) -> Notifier:
        """Factory method -> returns an instance of the Notifier class"""
        pass

    def send(self, message: str) -> None:
        notifier = self.create_notifier()
        notifier.send(message)


class EmailNotifierService(NotifierService):
    def create_notifier(self) -> Notifier:
        return EmailNotifier()


class SMSNotifierService(NotifierService):
    def create_notifier(self) -> Notifier:
        return SMSNotifier()


class PushNotifierService(NotifierService):
    def create_notifier(self) -> Notifier:
        return PushNotifier()


if __name__ == "__main__":
    email_service = EmailNotifierService()
    email_service.send("Hello, this is an email notification")

    sms_service = SMSNotifierService()
    sms_service.send("Hello, this is an SMS notification")

    push_service = PushNotifierService()
    push_service.send("Hello, this is a push notification")
