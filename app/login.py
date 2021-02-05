from authentication import Atuhtenticator
from utils import *
import sys
auth = Atuhtenticator()

class LoginMask:
    
    def loginMaskOperator(self):
        state = input("Wollen Sie sich anmelden oder als Benutzer fortfahren? (y/n)")
        if state == "y":
            un = input("Benutzername eingeben:")
            pw = input("Passwort eingeben:")
            if auth.isTranslator(un, pw):
                print("Wilkommen Translator!")
            elif auth.isAdmin(un, pw):
                print("Wilkommen Admin!")
            else: 
                continueState = input("Ups, Sie scheinen nicht registriert zu sein. Wollen Sie als User fortfahren? (y/n)")
                if continueState == "y":
                    print("Wilkommen User!")
                else:
                    print("Auf Wiedersehen!")
                    sys.exit()
        else:
            print("Hallo User!")