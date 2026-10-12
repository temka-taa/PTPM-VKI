import os
import sys
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from valid import valid
from database import w_DB
from controller import Controller


class StubInput:
    def __init__(self, login, password, a_passw):
        self.data = (login, password, a_passw)

    def get_data(self):
        return self.data


class TestController(unittest.TestCase):
    def setUp(self):
        self.db = w_DB()                     # настоящая БД (в памяти, своя для каждого теста)
        self.sender = Mock()                 # ЗАГЛУШКА отправки
        self.input = StubInput("Test_user1", "Пароль123!", "Пароль123!")   # ЗАГЛУШКА ввода
        self.validator = valid()             # настоящий валидатор
        self.controller = Controller(self.validator, self.input, self.db, self.sender)