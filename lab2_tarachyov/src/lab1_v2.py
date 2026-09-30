# import # logging
import re
import sys
import hashlib

def lgn(login, passw, A_passw ):
    def mask(p):
        return hashlib.sha256(p.encode("utf-8")).hexdigest()[:12]
    res_msg = ""
    res_bool = False


    try:
        black_list = ['89537846735', 'artem.tarachev2@gmail.com', '89999999999']
        login_ok = True

        if len(login)< 5:
            res_msg = 'Login too short'
            login_ok = False
        elif login in black_list:
            res_msg = 'Login is bad(blacklist)'
            login_ok = False
        elif login_ok:
            if "@" in login:
                if re.fullmatch(r"^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$", login):
                    login_ok = True
                else:
                    res_msg = 'Non correct email format "exsample@exampl.com"'
                    login_ok = False
            elif login[0] in "8":
                if re.fullmatch(r"^8\d{10}$", login):
                    login_ok = True
                else:
                    res_msg = 'Non correct number format "8xxxxxxxxxx"'
                    login_ok = False
            elif login[0] in "+":
                if re.fullmatch(r"^\+7-\d{3}-\d{3}-\d{2}\d{2}$", login):
                    login_ok = True
                else:
                    res_msg = 'Non correct number format "+7-xxx-xxx-xxxx"'
                    login_ok = False
            else:
                a = b = c = err = False
                for i in login:
                    if re.fullmatch(r"[A-Za-z]",i):
                        a = True
                    elif re.fullmatch(r"\d",i):
                        b = True
                    elif re.fullmatch(r"_",i):
                        c = True
                    else:
                        err = True
                if not a :
                    res_msg = 'Login without letter'
                    login_ok = False
                elif not b :
                    res_msg = 'Login without numbers'
                    login_ok = False
                elif not c :
                    res_msg = 'Login without "_" simbols'
                    login_ok = False
                elif err :
                    res_msg = 'Login with cirilic letter'
                    login_ok = False
                else:
                    login_ok = True
        if not login_ok and res_msg == "":
            res_msg = 'Login no pattern matched'
        elif res_msg != "":
            res_bool = False
        else:
            if len(passw) < 7:
                res_msg = 'Password too short'
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
                elif not b : res_msg = 'Password not small letter'
                elif not c : res_msg = 'Password not numbers'
                elif not d : res_msg = 'Password not special simbols'
                elif passw != A_passw : res_msg = 'Second password not matched'
                if res_msg == '':
                    res_bool = True
    except Exception:
        res_bool = False
        res_msg = 'Internal error'
    # print(res_bool)
    # print(res_msg)
    return res_bool, res_msg