import unittest

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
        ok, msg = lgn("899999991901", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(msg, 'Non correct number format "8xxxxxxxxxx"')
        print('\n')

    def test_lForm2(self):
        ok, msg = lgn("+79199999999", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(msg, 'Non correct number format "+7-xxx-xxx-xxxx"')
        print('\n')

    def test_lForm3(self):
        ok, msg = lgn("asdasd@afsasfasf", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(msg, 'Non correct email format "exsample@exampl.com"')
        print('\n')

    def test_lForm4(self):
        ok, msg = lgn("12342353_", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(msg, 'Login without letter')
        print('\n')

    def test_lForm5(self):
        ok, msg = lgn("lolo12lolo", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(msg, 'Login without "_" simbols')
        print('\n')

    def test_lForm6(self):
        ok, msg = lgn("hihihihi_", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(msg, "Login without numbers")
        print('\n')

    def test_lForm7(self):
        ok, msg = lgn("Яlogin_1233", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(msg, 'Login with cirilic letter')
        print('\n')

    def test_valid_phone8(self):
        ok, msg = lgn("89999999919", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, True)
        self.assertEqual(msg, "")

    def test_valid_phoneDashed(self):
        ok, msg = lgn("+7-123-456-7890", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, True)
        self.assertEqual(msg, "")

    def test_valid_email(self):
        ok, msg = lgn("user@mail.ru", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, True)
        self.assertEqual(msg, "")
if __name__ == "__main__":
    unittest.main()