import logging
import re
import sys
import hashlib

def mask(p):
    return hashlib.sha256(p.encode("utf-8")).hexdigest()[:12]
try:
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
    l_err = None
    login_ok = False

    log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"
    logging.basicConfig(
        level=logging.DEBUG,
        format=log_format,
        datefmt=date_format,
        force=True,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("log/file_txt.log", encoding="utf-8")
        ]
    )
    logging.info("Логгер успешно сконфигурирован")
    logging.info("Приложение запущено")


    if len(login)< 5:
        l_err = 'Login too short'
        logging.error(f'Login={login} | error: {l_err}')
    elif login in black_list:
        l_err = 'Login is bad(blacklist)'
        logging.error(f'Login={login} | error: {l_err}')
    else:
        logging.debug(f'Start login check for format | login={login}')
        for i in patterns.keys():
            # print(f'l: {login},i:  {i }')
            match re.fullmatch(i, login):
                case re.Match():
                    # print(login)
                    login_ok = True
                    break
                case _:
                    logging.warning(f'Login {login} not matched, because {patterns[i]}')
                    pass
    if login_ok:
        logging.info(f'Login successful: {login}')
    else: logging.error(f'Login failed: {login} | reason: {l_err or "no pattern matched"}')
    logging.info(f'Start password check | login {login}')
    if len(passw) < 7:
        logging.error(f'Login={login} | error: Password too short | pass={mask(passw)}')
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
        if err : logging.error(f'Login={login} | Password = {mask(passw)} with Latin letter')
        elif not a : logging.error(f'Login={login} | Password = {mask(passw)} not big letter')
        elif not b : logging.error(f'Login={login} | Password = {mask(passw)} not small letter')
        elif not c : logging.error(f'Login={login} | Password = {mask(passw)} not numbers')
        elif not d : logging.error(f'Login={login} | Password = {mask(passw)} not special simbols')
        elif passw != A_passw : logging.error(f'Login={login} | Password = {mask(passw)} Second password not matched')
        else:
            logging.info(f'Login={login} | pass={mask(passw)}')
        print(result_bool)
        print(result_msg)
except Exception:
    logging.exception("Unhandled exception")
