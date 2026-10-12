from abc import ABC, abstractmethod

class ISender(ABC):
    @abstractmethod
    def send(self, text):
        pass

class EmailSender(ISender):
    def send(self, text):
        return "Sent: " + text