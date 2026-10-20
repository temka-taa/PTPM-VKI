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
        self.db = w_DB()
        self.sender = Mock()
        self.input = StubInput("Test_user1", "Пароль123!", "Пароль123!")
        self.validator = valid()
        self.controller = Controller(self.validator, self.input, self.db, self.sender)

    def test_new_data_computed_and_saved(self):
        result, msg = self.controller.run()
        self.assertEqual(result, True)
        self.assertEqual(msg, "")
        self.assertTrue(self.sender.send.called)
        row = self.db.get("Test_user1", "Пароль123!", "Пароль123!")
        self.assertIsNotNone(row)

    def test_existing_data_taken_from_db(self):
        self.controller.run()
        with patch.object(self.validator, "valid") as spy:
            result, msg = self.controller.run()
            spy.assert_not_called()

    def test_sender_receives_correct_message(self):
        self.controller.run()
        sent_text = self.sender.send.call_args.args[0]
        self.assertIn("Test_user1", sent_text)

    def test_db_add_get_delete(self):
        self.db.add("log1", "pass1", "pass1", True, "")
        row = self.db.get("log1", "pass1", "pass1")
        self.assertIsNotNone(row)

        self.db.delete("log1", "pass1", "pass1")
        row = self.db.get("log1", "pass1", "pass1")
        self.assertIsNone(row)

    def test_db_get_missing_returns_none(self):
        row = self.db.get("no_such", "no_such", "no_such")
        self.assertIsNone(row)