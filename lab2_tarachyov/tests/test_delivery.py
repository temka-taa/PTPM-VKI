import unittest
from Delivery import calculate_delivery_cost


class TestDeliv(unittest.TestCase):
    def test_weightMin(self):
        cost, date = calculate_delivery_cost(0.01, 10, "обычный", True)
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")
        print('\n')

    def test_weightMax(self):
        cost, date = calculate_delivery_cost(51.0, 10, "обычный", True)
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")
        print('\n')

    def test_distanceMin(self):
        cost, date = calculate_delivery_cost(1.1, 0, "обычный", True)
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")
        print('\n')

    def test_distanceMax(self):
        cost, date = calculate_delivery_cost(1.1, 5001, "обычный", True)
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")
        print('\n')

    def test_badType(self):
        cost, date = calculate_delivery_cost(1.1, 10, "стекло")
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")
        print('\n')

    def test_normalCost(self):
        cost, date = calculate_delivery_cost(1.1, 10, "обычный")
        self.assertEqual(cost, 250)
        self.assertEqual(date, "2026-09-04")
        print('\n')

    def test_midWeightCost(self):
        cost, date = calculate_delivery_cost(5.1, 10, "обычный")
        self.assertEqual(cost, 300)
        self.assertEqual(date, "2026-09-04")
        print('\n')

    def test_heavyWeightCost(self):
        cost, date = calculate_delivery_cost(20, 10, "обычный")
        self.assertEqual(cost, 375)
        self.assertEqual(date, "2026-09-04")
        print('\n')

    def test_fragileCost(self):
        cost, date = calculate_delivery_cost(1.1, 10, "хрупкий")
        self.assertEqual(cost, 550)
        self.assertEqual(date, "2026-09-04")
        print('\n')

    def test_dangerousCost(self):
        cost, date = calculate_delivery_cost(1.1, 10, "опасный")
        self.assertEqual(cost, 1250)
        self.assertEqual(date, "2026-09-04")
        print('\n')


class test_bugs(unittest.TestCase):
    def test_expressCost(self):
        cost, date = calculate_delivery_cost(1.1, 10, "обычный", True)
        self.assertGreater(cost, 250)
        print('\n')

    def test_expressDays(self):
        cost, date = calculate_delivery_cost(1.1, 500, "обычный", True)
        self.assertNotEqual(date, "2026-09-03")

    def test_expressOneDay(self):
        self.assertEqual(calculate_delivery_cost(1, 100, "обычный", True)[1], "2026-09-04")


if __name__ == "__main__":
    unittest.main()