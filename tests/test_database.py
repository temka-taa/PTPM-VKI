import sqlite3
import unittest

from src.database import DatabaseRepository


class TestDB(unittest.TestCase):
    def setUp(self):
        self.repo = DatabaseRepository(':memory:')

    def tearDown(self):
        self.repo.close()

    def test_add(self):
        self.assertTrue(self.repo.add(1, 'user1', 'hi'))

    def test_add_dup(self):
        self.repo.add(1, 'user1', 'hi')
        with self.assertRaises(sqlite3.IntegrityError):
            self.repo.add(1, 'user2', 'hello')

    def test_get_by_id(self):
        self.repo.add(1, 'user1', 'hi')
        self.assertEqual(self.repo.get_by_id(1)['name'], 'user1')

    def test_get_by_id_none(self):
        self.assertIsNone(self.repo.get_by_id(999))

    def test_get_by_name(self):
        self.repo.add(1, 'user1', 'a')
        self.repo.add(2, 'user1', 'b')
        self.assertEqual(len(self.repo.get_by_name('user1')), 2)

    def test_get_by_name_empty(self):
        self.assertEqual(self.repo.get_by_name('nobody'), [])

    def test_update(self):
        self.repo.add(1, 'user1', 'old')
        self.assertTrue(self.repo.update(1, 'new'))

    def test_update_none(self):
        self.assertFalse(self.repo.update(999, 'new'))

    def test_delete(self):
        self.repo.add(1, 'user1', 'hi')
        self.assertTrue(self.repo.delete(1))

    def test_delete_none(self):
        self.assertFalse(self.repo.delete(999))


if __name__ == '__main__':
    unittest.main()