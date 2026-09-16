import logging
import re
import sys

logging.basicConfig(level=logging.DEBUG)

login = input('Email, number or login: ')
passw = input('Enter your password: ')
A_passw = input("Enter your password again: ")
patterns = {
    r"^\+7\d{10}$":'Non correct number format "+7xxxxxxxxxx"',
    r"^8\d{10}$": 'Non correct number format "8xxxxxxxxxx"',
    r"^\+7-\d{3}-\d{3}-\d{2}\d{2}$":'Non correct number format "+7-xxx-xxx-xxxx"',
    r"^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$": 'Non correct email format "exsample@exampl.com"' ,
    r"^(?=.*[A-Za-z])(?=.*\d)(?=.*_)[A-Za-z0-9_]+$":'Non correct login (Cyrillic simbols or not numbers or not "_") '
}
black_list = ['89537846735', 'artem.tarachev2@gmail.com']

log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(
    level=logging.DEBUG,
    format=log_format,
    datefmt=date_format,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("log/file_txt.log", encoding="utf-8")
    ]
)
logging.info("Логгер успешно сконфигурирован")
logging.info("Приложение запущено")

if len(login)< 5:
    logging.error('Login to short')
elif login in black_list:
    logging.error('Login is bad(blacklist)')
else:
    logging.debug('Start login check for format')
    for i in patterns.keys():
        print(f'l: {login},i:  {i }')
        match re.fullmatch(i, login):
            case re.Match():
                print(login)
                break
            case _:
                logging.warning(f'Login {login} not matched, because {patterns[i]}')
                pass

logging.info(f'Login successful: {login}')
logging.info('Start password check')
if len(passw) < 7:
    logging.error('Password to short')
else:
    a = b = c = d = err = False
    for i in passw:
        if re.fullmatch(r"[А-ЯЁ]", i):
            a = True
        elif re.fullmatch(r"[а-яё]", i):
            b = True
        elif re.fullmatch(r"\d", i):
            c = True
        elif re.fullmatch(r"[^A-Za-z0-9А-Яа-яЁё]", i):
            d = True
        else:
            err = True
    if a and b and c and d and not err:
        if passw == A_passw:
            print('Password matched')
        else :
            print('Second password not matched')
    else:
        print('Incorrect password format!')
        logging.log('Incorrect password format!')