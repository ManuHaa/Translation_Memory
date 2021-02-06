from login.authentication import Atuhtenticator
from utils import *
from operators.userOperator import UserOperator
import sys
auth = Atuhtenticator()
user = UserOperator()

class LoginMask:

    def loginMaskOperator(self):
        operator = { "operator" : None}
        state = input("Wollen Sie sich anmelden oder als Benutzer fortfahren? (y/n)")
        if state == "y":
            un = input("Benutzername eingeben:")
            pw = input("Passwort eingeben:")
            if auth.isTranslator(un, pw):
                print("Wilkommen Translator!")
                operator['operator'] = "translator"
                return operator
            elif auth.isAdmin(un, pw):
                print("Wilkommen Admin!")
                operator['operator'] = "admin"
                return operator
            else: 
                continueState = input("Ups, Sie scheinen nicht registriert zu sein. Wollen Sie als User fortfahren? (y/n)")
                if continueState == "y":
                    print("Wilkommen User!")
                    operator['operator'] = "user"
                    return operator
                else:
                    print("Auf Wiedersehen!")
                    sys.exit()
        elif state == "n":
            print("Hallo User!")
            operator['operator'] = "user"
            return operator
        else:
            print("Ups, Ihre Eingabe war fehlerhaft.")
            sys.exit()


            