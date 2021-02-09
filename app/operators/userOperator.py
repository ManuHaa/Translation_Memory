import sys
from pathlib import Path
root = Path(__file__).parent.parent
objPath = str(root) + '/obj'
sys.path.insert(1, objPath)
from user import User
from pattern.singleton import Singleton

user = User()

class UserOperator(metaclass=Singleton):

    def operate(self):
        operation = input("Was möchten Sie tun?(1/2/3/4)\n 1. Nach einem Wort suchen\n 2. Anzahl angelegter Wörter anzeigen\n 3. Alle registrierten Wörter anzeigen lassen\n 4. Applikation schließen \n Eingabe: ")
        if operation.isdigit():
            if operation == "1":
                word = input("Bitte geben Sie ein Wort ein: ")
                if word.isalpha(): 
                    if user.wordExists(word):
                        translation = user.showTranslations(word)
                    else:
                        state = input("Das eingegebene Wort existiert noch nicht. Wollen Sie es anlegen damit ein Übersetzer es übersetzen kann?(y/n)")
                        if state == "y":
                            user.addWord(word)
                            user.updateUserAddedWords()
                            print("Das Wort wurde erfolgreich hinzugefügt!")
                else:
                    print('Ihre Eingabe war leider kein valides Wort.')
            elif operation == '2':
                if user.showNumberOfAddedWords("user") is None:
                    print("Sie haben bisher noch keine Wörter angelegt.")
                else:
                    user.showNumberOfAddedWords("user")
            elif operation == '3': 
                user.showNumberOfRegisteredWords()
            else:
                print("Auf Wiedersehen!")
                sys.exit()
        else:
            print("Fehlerhafte Eingabe.")
            

    