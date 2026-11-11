import unittest
from pathlib import Path
from unittest.mock import patch

from src.database import DatabaseRepository
from src.parcer import ForumParser

HTML = '''
<article id="1" class="tm-articles-list__item">
  <a class="tm-user-info__username">user1</a>
  <a class="tm-title__link"><span>First</span></a>
</article>
<article id="2" class="tm-articles-list__item">
  <a class="tm-user-info__username">user2</a>
  <a class="tm-title__link"><span>Second</span></a>
</article>
'''

FIXTURE = Path(__file__).parent / 'fixtures' / 'forum_page.html'


class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = ForumParser('https://habr.com/ru/feed/', None)

    @patch('src.parcer.requests.get')
    def test_parse(self, get):
        get.return_value.text = HTML
        posts = self.parser.parse_page('https://habr.com/ru/feed/')
        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0]['name'], 'user1')

    @patch('src.parcer.requests.get')
    def test_save(self, get):
        get.return_value.text = HTML
        repo = DatabaseRepository(':memory:')
        posts = self.parser.parse_page('https://habr.com/ru/feed/')
        self.parser.save_to_db(posts, repo)
        self.assertEqual(repo.get_by_id(1)['message'], 'First')
        repo.close()


if __name__ == '__main__':
    unittest.main()