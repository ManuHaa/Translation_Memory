import sys
import os
from pathlib import Path
root = Path(__file__).parent.parent
objPath = str(root) + '/obj'
sys.path.insert(1, objPath)
from user import User

user = User()

class UserOperator:

    def operate(self):
        operation = input("Was möchten Sie tun?(1/2/3)\n 1. Nach einem Wort suchen\n 2. Anzahl angelegter Wörter anzeigen\n 3. Alle registrierten Wörter anzeigen lassen\n Eingabe: ")
        if operation == "1":
            word = input("Bitte geben Sie ein Wort ein.")
            if user.wordExists(word):
                translation = user.showTranslations(word)
            else:
                print("Das eingegebene Wort existiert noch nicht. Wollen Sie es anlegen damit ein Übersetzer es übersetzen kann?")
            

    