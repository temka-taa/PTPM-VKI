#1. подтягиваем сторонние библеотеки через виртуальное окружение
# py -m venv venv
#2. lib папка со сторонними библеотеками
# scripts бинарники котоорые можем запускать python.exe используется для проекта, наш виртуальный,
#3. Активируем окружение .\venv\Scripts\activate
# аналог браузера нужен pip install requests
# в lib появилась requests и несколько библеотек для зависимостей
# снизу справа inter sett ->add interp-> находим ео в файле scripts
import requests

# resp = requests.get('https://4pda.to/')

#print(resp) #проверяем
# запуск py .\ex_parcer.py
#print(resp.text) #html разметка

# библеотека pip install beautifulsoup4
import bs4 #импортируем ее
# url = 'https://habr.com/ru/feed/'

class ForumParser:
    def __init__(self,url,repo):
        self.url = 'https://habr.com/ru/feed/'
        self.repo = repo
    def parse_page(self, url: str):
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
                " like Gecko) Chrome/124.0.0.0 Safari/537.36"
            )
        }
        resp = requests.get(self.url, headers=headers, timeout=10)
        # print(resp.text)
        bs = bs4.BeautifulSoup(resp.text, 'html.parser') #'html.parser' для режима работы
        all_posts = bs.find_all('article', class_='tm-articles-list__item') #ищем все обьекты с тегом див и атрибутами ищем карточки
        parsed_data = []
        for post in all_posts:
            id_ = post.get('id')
            autor_login = post.find('a', class_='tm-user-info__username').text
            mess = post.find('a', class_='tm-title__link')
            if mess:
                message = mess.find('span').text # вот тут конкретно
            else:
                message = 'Rate not found'
        #     print(f" id - {id_}, L - {autor_login} , mess - {message}" )                        !!!!!!!!

            parsed_data.append({
                'id': int(id_),
                'name': autor_login,
                'message': message,
            })
            return parsed_data
    def save_to_db(self, parse_data, repo):
        for item in parse_data:
            repo.add(item["id"],item["name"], item["message"])

# .\venv\ не должно быть в репо
# pip freeze какие библ есть в окружении
# чтоб зафиксировать их pip freeze >> requirements.txt
# чтоб установить делаем все с самого начала но для установки нужных зависимостей
# .\venv\scripts\activate
# pip install -r requirements.txt