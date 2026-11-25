import unittest
import time
from selenium import webdriver

from pages.calculator_page import CalculatorPage


class CalculatorTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(5)
        self.page = CalculatorPage(self.driver)
        self.page.open()

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

    def check(self, a, b, op, expected):
        self.page.calculate(a, b, op)
        expected_line = f"{a} {op} {b} = {expected}"
        self.page.wait_forres(expected_line)
        self.assertEqual(self.page.getres(), expected_line)

    def test_addition(self):
        self.check(7, 5, "+", 12)

    def test_subtraction(self):
        self.check(10, 3, "-", 7)

    def test_multiplication(self):
        self.check(6, 4, "*", 24)

    def test_division(self):
        self.check(20, 4, "/", 5)

    def test_division_by_zero(self):
        self.check(10, 0, "/", "null")

    def test_zero_values(self):
        self.check(0, 0, "+", 0)

    def test_negative_values(self):
        self.check(-5, 3, "+", -2)

    def test_decimal_values(self):
        self.check(2.5, 2, "*", 5)

    def test_increment_decrement_buttons(self):
        self.page.clickinc_a()
        self.page.wait_forres("1 + 0 = 1")
        self.assertEqual(self.page.getres(), "1 + 0 = 1")

        self.page.clickdec_b()
        self.page.wait_forres("1 + -1 = 0")
        self.assertEqual(self.page.getres(), "1 + -1 = 0")