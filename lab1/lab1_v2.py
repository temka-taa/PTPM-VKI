import logging
import re
logging.basicConfig(level=logging.DEBUG)

login = input('Email or number: ')
passw = input('Enter your password: ')
A_passw = input("Enter your password again: ")
l_patterns = [r"^\+7\d{10}$",r"^8\d{10}$",
           r"^\+7\s\(\d{3}\)\s\d{3}\s\d{2}\s\d{2}$",
           r"^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$"]
p_patterns = [r"",]
black_list = ['89537846735', 'artem.tarachev2@gmail.com']


if len(login)< 5:
    print('Login failed')

elif login in black_list:
    print('Login failed ')
else:
    for i in l_patterns:
        match re.fullmatch(i, login):
            case re.Match():
                print(login)
                break
            case _:
                pass
if len(passw) < 7:
    print('Password failed')

