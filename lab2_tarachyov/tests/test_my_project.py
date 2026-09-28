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

    def test_shortLogin(self):
        ok, msg = lgn("abc", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(msg, "Login too short")
        print('\n')

    def test_blacklistLogin(self):
        ok, msg = lgn("89999999999", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(msg, "Login is bad(blacklist)")
        print('\n')

    def test_pattern(self):
        ok, msg = lgn("собака", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(msg, "Login no pattern matched")
        print('\n')

    def test_passwSize(self):
        ok, msg = lgn("89999999991", "", "")
        self.assertEqual(ok, False)
        self.assertEqual(msg, "Password too short")
        print('\n')

    def test_passwLatin(self):
        ok, msg = lgn("89999999919", "Passw123!", "passw123!")
        self.assertEqual(ok, False)
        self.assertEqual(msg, "Password with Latin letter")
        print('\n')

    def test_paswBig(self):
        ok, msg = lgn("89999999919", "пароль123!", "пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(msg, "Password not big letter")
        print('\n')

    def test_paswSmall(self):
        ok, msg = lgn("89999999919", "ПАРОЛЬ123!", "ПАРОЛЬ123!")
        self.assertEqual(ok, False)
        self.assertEqual(msg, "Password not small letter")
        print('\n')

    def test_paswNum(self):
        ok, msg = lgn("89999999919", "Пароль!", "Пароль!")
        self.assertEqual(ok, False)
        self.assertEqual(msg, "Password not numbers")
        print('\n')

    def test_paswSimv(self):
        ok, msg = lgn("89999999919", "Пароль123", "Пароль123")
        self.assertEqual(ok, False)
        self.assertEqual(msg, "Password not special simbols")
        print('\n')

    def test_paswSecond(self):
        ok, msg = lgn("89999999919", "Пароль123!", "Парольь123!")
        self.assertEqual(ok, False)
        self.assertEqual(msg, "Second password not matched")
        print('\n')

    def test_lForm1(self):
        ok, msg = lgn("89999999919", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(msg, "Non correct number format '+7xxxxxxxxxx'")
        print('\n')

    def test_lForm2(self):
        ok, msg = lgn("+79199999999", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(msg, "Non correct number format '8xxxxxxxxxx'")
        print('\n')

    def test_lForm3(self):
        ok, msg = lgn("89999999919", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(msg, "Non correct number format '+7-xxx-xxx-xxxx'")
        print('\n')

    def test_lForm4(self):
        ok, msg = lgn("asdasd@afsasfasf", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(msg, "Non correct email format 'exsample@exampl.com'")
        print('\n')

    def test_lForm5(self):
        ok, msg = lgn("првиет12привет", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(msg, "Non correct login (Cyrillic simbols or not numbers or not '_')")
        print('\n')

    # def test_(self):
    #     ok, msg = lgn("", "", "")
    #     self.assertEqual(ok, False)
    #     self.assertEqual(msg, "")
    #     print('\n')
    #
    # def test_(self):
    #     ok, msg = lgn("", "", "")
    #     self.assertEqual(ok, False)
    #     self.assertEqual(msg, "")
    #     print('\n')
    #
    # def test_(self):
    #     ok, msg = lgn("", "", "")
    #     self.assertEqual(ok, False)
    #     self.assertEqual(msg, "")
    #     print('\n')
    #
    # def test_(self):
    #     ok, msg = lgn("", "", "")
    #     self.assertEqual(ok, False)
    #     self.assertEqual(msg, "")
    #     print('\n')
if __name__ == "__main__":
    unittest.main()