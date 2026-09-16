import logging
import re
logging.basicConfig(level=logging.DEBUG)

login = input('Email or number: ')
passw = input('Enter your password: ')
A_passw = input("Enter your password again: ")
patterns = {
    r"^\+7\d{10}$":'Non correct number',
    r"^8\d{10}$": 'Non correct number',
    r"^\+7\s\(\d{3}\)\s\d{3}\s\d{2}\d{2}$":'Non correct number',
    r"^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$": 'Non correct email',
    r"^[A-Za-z0-9_]+$":'Non correct login'
}
black_list = ['89537846735', 'artem.tarachev2@gmail.com']
log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

if len(login)< 5:
    print('Login failed')
elif login in black_list:
    print('Login failed')
else:
    for i in patterns.keys():
        print(f'l: {login},i:  {i }')
        match re.fullmatch(i, login):
            case re.Match():
                print(login)
                break
            case _:
                pass

if len(passw) < 7:
    print('Password to short')
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