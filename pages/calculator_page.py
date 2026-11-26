from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
import time

class CalculatorPage:
    # url = "https://www.globalsqa.com/angularJs-protractor/SimpleCalculator/"
    url = "file:///g%3A/pr1/calc.html"
    a = (By.CSS_SELECTOR, 'input[ng-model="a"]')
    b = (By.CSS_SELECTOR, 'input[ng-model="b"]')
    oper = (By.CSS_SELECTOR, 'select[ng-model="operation"]')
    res = (By.CSS_SELECTOR, "b.result")
    inc_a = (By.CSS_SELECTOR, 'button[ng-click="inca()"]')
    dec_a = (By.CSS_SELECTOR, 'button[ng-click="deca()"]')
    inc_b = (By.CSS_SELECTOR, 'button[ng-click="incb()"]')
    dec_b = (By.CSS_SELECTOR, 'button[ng-click="decb()"]')

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def enter_a(self, value):
        field = self.driver.find_element(*self.a)
        field.clear()
        field.send_keys(str(value))

    def enter_b(self, value):
        field = self.driver.find_element(*self.b)
        field.clear()
        field.send_keys(str(value))

    def selectoper(self, op):
        select = Select(self.driver.find_element(*self.oper))
        select.select_by_value(op)

    def clickinc_a(self):
        self.driver.find_element(*self.inc_a).click()

    def clickdec_a(self):
        self.driver.find_element(*self.dec_a).click()

    def clickinc_b(self):
        self.driver.find_element(*self.inc_b).click()

    def clickdec_b(self):
        self.driver.find_element(*self.dec_b).click()

    def calculate(self, a, b, op):
        self.enter_a(a)
        time.sleep(0.5)
        self.enter_b(b)
        time.sleep(0.5)
        self.selectoper(op)
        time.sleep(0.5)

    def getres(self):
        return self.driver.find_element(*self.res).text
    def wait_forres(self, expected_text):
        WebDriverWait(self.driver, 5).until(
            lambda driver: driver.find_element(*self.res).text == expected_text
        )