import sys
from pathlib import Path
root = Path(__file__).parent.parent
objPath = str(root) + '/obj'
sys.path.insert(1, objPath)
from user import User
from pattern.singleton import Singleton
#from utils import Colors as c
from obj.colors import Colors as color
user = User()

class UserOperator(metaclass=Singleton):

    def operate(self):
        operation = input(color.yellow + "Was möchten Sie tun?(1/2/3/4)\n " + color.end + "1. Nach einem Wort suchen\n 2. Anzahl angelegter Wörter anzeigen\n 3. Anzahl aller registrierter Wörter anzeigen mit Anzahl komplett übersetzer Wörter\n 4. Applikation schließen \n" + color.yellow + "Eingabe: " + color.end)
        if operation.isdigit():
            if operation == '1':
                word = input("Bitte geben Sie ein Wort ein: ")
                if word.isalpha(): 
                    if user.wordExists(word):
                        translation = user.showTranslations(word)
                    else:
                        state = input(color.yellow + "Das eingegebene Wort existiert noch nicht. Wollen Sie es anlegen damit ein Übersetzer es übersetzen kann?(y/n)\n" + color.end  +  "Eingabe: ")
                        if state == 'y':
                            user.addWord(word)
                            user.updateUserAddedWords()
                            print(color.green + "Das Wort wurde erfolgreich hinzugefügt!"  + color.end)
                else:
                    print(color.red + "Ihre Eingabe war leider kein valides Wort." + color.end)
            elif operation == '2':
                if user.showNumberOfAddedWords("user") is None:
                    print(color.yellow + "Sie haben bisher noch keine Wörter angelegt." + color.end)
                else:
                    user.showNumberOfAddedWords("user")
            elif operation == '3': 
                user.showNumberOfRegisteredWords()
            else:
                print(color.blue + "Auf Wiedersehen!" + color.end)
                sys.exit()
        else:
            print(color.red + "Fehlerhafte Eingabe." + color.end)
            

    