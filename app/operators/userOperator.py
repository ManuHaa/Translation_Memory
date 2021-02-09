import sys
from pathlib import Path
root = Path(__file__).parent.parent
objPath = str(root) + '/obj'
sys.path.insert(1, objPath)
from user import User
from pattern.singleton import Singleton
from utils import Colors as c

user = User()

class UserOperator(metaclass=Singleton):

    def operate(self):
        operation = input(c.yellow + "Was möchten Sie tun?(1/2/3/4)\n " + c.end + "1. Nach einem Wort suchen\n 2. Anzahl angelegter Wörter anzeigen\n 3. Alle registrierten Wörter anzeigen lassen\n 4. Applikation schließen \n" + c.yellow + "Eingabe: " + c.end)
        if operation.isdigit():
            if operation == '1':
                word = input("Bitte geben Sie ein Wort ein: ")
                if word.isalpha(): 
                    if user.wordExists(word):
                        translation = user.showTranslations(word)
                    else:
                        state = input(c.yellow + "Das eingegebene Wort existiert noch nicht. Wollen Sie es anlegen damit ein Übersetzer es übersetzen kann?(y/n)\n" + c.end  +  "Eingabe: ")
                        if state == 'y':
                            user.addWord(word)
                            user.updateUserAddedWords()
                            print(c.green + "Das Wort wurde erfolgreich hinzugefügt!"  + c.end)
                else:
                    print(c.red + "Ihre Eingabe war leider kein valides Wort." + c.end)
            elif operation == '2':
                if user.showNumberOfAddedWords("user") is None:
                    print(c.yellow + "Sie haben bisher noch keine Wörter angelegt." + c.end)
                else:
                    user.showNumberOfAddedWords("user")
            elif operation == '3': 
                user.showNumberOfRegisteredWords()
            else:
                print(c.blue + "Auf Wiedersehen!" + c.end)
                sys.exit()
        else:
            print(c.red + "Fehlerhafte Eingabe." + c.end)
            

    