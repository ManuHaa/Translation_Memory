from login.authentication import Atuhtenticator
from operators.userOperator import UserOperator
from utils import Colors as color
import sys

auth = Atuhtenticator()
user = UserOperator()

class LoginMask:

    def loginMaskOperator(self):
        operator = { "operator" : None}
        state = input(color.blue + "TranslationMemory\n" + color.end + "Wilkommen!\nWollen Sie sich anmelden oder als Benutzer fortfahren? (y/n) \n" + color.yellow + "Eingabe: " +  color.end)
        if state == 'y':
            username = input("Benutzername eingeben: ")
            password = input("Passwort eingeben: ")
            if auth.isTranslator(username, password):
                print(color.green + "Wilkommen Translator!" + color.end)
                operator['operator'] = "translator"
                return operator
            elif auth.isAdmin(username, password):
                print(color.green + "Wilkommen Admin!" + color.end)
                operator['operator'] = "admin"
                return operator
            else: 
                continueState = input(color.yellow + "Ups, Sie scheinen nicht registriert zu sein. Wollen Sie als User fortfahren?(y/n) \n" + color.end + "Eingabe: ")
                if continueState == 'y':
                    print(color.green + "Wilkommen User!" + color.end)
                    operator['operator'] = "user"
                    return operator
                else:
                    print(color.red + "Auf Wiedersehen!" + color.end)
                    sys.exit()
        elif state == 'n':
            print(color.green + "Wilkommen User!" + color.end)
            operator['operator'] = "user"
            return operator
        else:
            print(color.blue + "Ups, Ihre Eingabe war fehlerhaft." + color.end)
            sys.exit()


            