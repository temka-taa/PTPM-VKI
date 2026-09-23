import os
import sys
import unittest

# sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from lab1_v2 import lgn


class TestMyProj(unittest.TestCase):
    def test_valid_login_and_password_passes(self):
        ok, msg = lgn("Test_user1", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, True)
        self.assertEqual(msg, "")
        print('\n')

    def test_short_login_fails(self):
        ok, msg = lgn("abc", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(msg, "Login too short")
        print('\n')


if __name__ == "__main__":
    unittest.main()