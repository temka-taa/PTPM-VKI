from abc import ABC, abstractmethod

class IInput(ABC):
    @abstractmethod
    def get_data(self):
        pass

class ConsoleInput(IInput):
    def get_data(self):
        log = input("Enter login: ")
        passw = input("Enter password: ")
        a_pass = input("Enter password again: ")
        return log,passw,a_pass