from login.authentication import Atuhtenticator
from operators.userOperator import UserOperator
import sys

auth = Atuhtenticator()
user = UserOperator()
color = '\033[93m'

class LoginMask:

    def loginMaskOperator(self):
        operator = { "operator" : None}
        state = input("TranslationMemory\nWilkommen! \nWollen Sie sich anmelden oder als Benutzer fortfahren? (y/n) \nEingabe: ")
        if state == 'y':
            username = input("Benutzername eingeben: ")
            password = input("Passwort eingeben: ")
            if auth.isTranslator(username, password):
                print("Wilkommen Translator!")
                operator['operator'] = "translator"
                return operator
            elif auth.isAdmin(username, password):
                print("Wilkommen Admin!")
                operator['operator'] = "admin"
                return operator
            else: 
                continueState = input("Ups, Sie scheinen nicht registriert zu sein. Wollen Sie als User fortfahren?(y/n) \nEingabe: ")
                if continueState == 'y':
                    print("Wilkommen User!")
                    operator['operator'] = "user"
                    return operator
                else:
                    print("Auf Wiedersehen!")
                    sys.exit()
        elif state == 'n':
            print("Wilkommen User!")
            operator['operator'] = "user"
            return operator
        else:
            print("Ups, Ihre Eingabe war fehlerhaft.")
            sys.exit()


            