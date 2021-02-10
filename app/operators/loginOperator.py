from obj.authentication import Atuhtenticator
from operators.userOperator import UserOperator
#from utils import Colors as color
from obj.colors import Colors as color
import sys

auth = Atuhtenticator()
user = UserOperator()

class LoginMask:
    currentUser = { "username": None, "password": None}
    def loginMaskOperator(self):
        operator = { "operator" : None}
        state = input(color.blue + "TranslationMemory\n" + color.end + "Wilkommen!\nWollen Sie sich anmelden oder als Benutzer fortfahren? (y/n) \n" + color.yellow + "Eingabe: " +  color.end)
        if state == 'y':
            username = input("Benutzername eingeben: ")
            password = input("Passwort eingeben: ")
            LoginMask.currentUser['username'] = username
            LoginMask.currentUser['password'] = password
            if username.isalnum() and password.isalnum():
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
                        print(color.blue + "Auf Wiedersehen!" + color.end)
                        sys.exit()
            else:
                operator['operator'] = "user"
                print(color.bold + "Ihre Eingabe war nicht valide, Sie werden nun als User eingeloggt.\n" + color.end + color.green + "Wilkommen User!" + color.end)
                return operator
        elif state == 'n':
            print(color.green + "Wilkommen User!" + color.end)
            operator['operator'] = "user"
            return operator
        else:
            print(color.blue + "Ups, Ihre Eingabe war fehlerhaft. Applikation wird automatisch beendet." + color.end)
            sys.exit()


            