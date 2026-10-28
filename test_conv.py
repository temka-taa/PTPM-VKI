import unittest
from Conventer import *

class TestConv(unittest.TestCase):
    def test_range(self):
        self.assertEqual(Conventer.do(150.0),1000)
    def test_range2(self):
        self.assertEqual(Conventer.do(100.7),1000)


    def test_range3(self):
        self.assertEqual(Conventer.do(65.7),65)
    def test_range4(self):
        self.assertEqual(Conventer.do(-0.5),-5)
    def test_range5(self):
        self.assertEqual(Conventer.do(-30.4),-35)
    def test_range6(self):
        self.assertEqual(Conventer.do(-30.5),-2000)

    def test_zero(self):
        with self.assertRaises(ValueError):
            Conventer.do(0.0)

if __name__ == '__main__':
    unittest.main()