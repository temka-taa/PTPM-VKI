# import # logging
import re
import sys
import hashlib

def lgn(login, passw, A_passw ):
    def mask(p):
        return hashlib.sha256(p.encode("utf-8")).hexdigest()[:12]
    # log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
    # date_format = "%Y-%m-%d %H:%M:%S"
    # # logging.basicConfig(
    #     level=# logging.DEBUG,
    #     format=log_format,
    #     datefmt=date_format,
    #     force=True,
    #     handlers=[
    #         # logging.StreamHandler(sys.stdout),
    #         # logging.FileHandler("log/file_txt.log", encoding="utf-8")
    #     ]
    # )
    # # logging.info("\n" * 5 )
    # # logging.info("Логгер успешно сконфигурирован")
    # # logging.info("Приложение запущено")

    res_msg = ""
    res_bool = False


    try:
        # login = input('Email, number or login: ')
        # passw = input('Enter your password: ')
        # A_passw = input("Enter your password again: ")
        patterns = {
            r"^\+7\d{10}$":'Non correct number format "+7xxxxxxxxxx"',
            r"^8\d{10}$": 'Non correct number format "8xxxxxxxxxx"',
            r"^\+7-\d{3}-\d{3}-\d{2}\d{2}$":'Non correct number format "+7-xxx-xxx-xxxx"',
            r"^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$": 'Non correct email format "exsample@exampl.com"' ,
            r"^(?=.*[A-Za-z])(?=.*\d)(?=.*_)[A-Za-z0-9_]+$":'Non correct login (Cyrillic simbols or not numbers or not "_") '
        }
        black_list = ['89537846735', 'artem.tarachev2@gmail.com']
        login_ok = True

        if len(login)< 5:
            res_msg = 'Login too short'
            # logging.error(f'Login={login} | error: {res_msg}')
            login_ok = False
        elif login in black_list:
            res_msg = 'Login is bad(blacklist)'
            # logging.error(f'Login={login} | error: {res_msg}')
            login_ok = False
        elif login_ok:
            # logging.debug(f'Start login check for format | login={login}')
            for i in patterns.keys():
                # print(f'l: {login},i:  {i }')
                match re.fullmatch(i, login):
                    case re.Match():
                        # print(login)
                        login_ok = True
                        break
                    case _:
                        login_ok = False
                        # logging.warning(f'Login {login} not matched, because {patterns[i]}')
                        pass
        if not login_ok and res_msg == "":
            res_msg = 'Login no pattern matched'
            # logging.error(f'Login failed: {login} | error: {res_msg}')
        elif res_msg != "":
            res_bool = False
        else:
            # logging.info(f'Login successful: {login}')
            # logging.info(f'Start password check | login {login}')
            if len(passw) < 7:
                res_msg = 'Password too short'
                # logging.error(f'Login={login} | error: {res_msg} | pass={mask(passw)}')
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
                if err : res_msg = 'Password with Latin letter'
                elif not a : res_msg = 'Password not big letter'
                elif not b : res_msg = 'Password  not small letter'
                elif not c : res_msg = 'Password not numbers'
                elif not d : res_msg = 'Password not special simbols'
                elif passw != A_passw : res_msg = 'Second password not matched'
                if res_msg == '':
                    res_bool = True
                    # logging.info(f'Login={login} | pass={mask(passw)} | result: second passw = {mask(passw)} matched')
                # else:
                    # logging.error(f'Login {login} | error: {res_msg} | pass={mask(passw)}')
    except Exception:
        # logging.exception("Unhandled exception")
        res_bool = False
        res_msg = 'Internal error'
    print(res_bool)
    print(res_msg)
    return res_bool, res_msg