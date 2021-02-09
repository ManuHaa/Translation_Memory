import sys
from pathlib import Path
root = Path(__file__).parent.parent
objPath = str(root) + '/obj'
sys.path.insert(1, objPath)
from translator import Translator

translator = Translator()

class TranslatorOperator:
    
    def operate(self):
        operation = input("Was möchten Sie tun?(1/2/3/4/5/6)\n 1. Nach einem Wort suchen\n 2. Anzahl angelegter Wörter anzeigen\n 3. Alle registrierten Wörter anzeigen lassen\n 4. Unkomplette Übersetzungen auflisten lassen\n 5. Anzahl eigener Übersetzungen anzeigen lassen\n 6. Applikation schließen \n Eingabe: ")
        if operation.isdigit():
            if operation == "1":
                word = input("Bitte geben Sie ein Wort ein: ")
                if word.isalpha():
                    if translator.wordExists(word):
                        translation = user.showTranslations(word)
                    else:
                        state = input("Das eingegebene Wort existiert noch nicht. Wollen Sie es anlegen?(y/n)")
                        if state == "y":
                            translator.addWord(word)
                            print("Das Wort wurde erfolgreich hinzugefügt!")
                else:
                    print("Ihre EIngabe war leider kein valides Wort.")
            elif operation == "2":
                if translator.showNumberOfAddedWords() is None:
                    print("Sie haben bisher noch keine Wörter angelegt.")
                else:
                    translator.showNumberOfAddedWords()
            elif operation == "3":
                translator.showNumberOfRegisteredWords()
            elif operation == '4':
                translator.getUncompleteTranslatedWords()
                state = input("Wollen Sie zu einem dieser Wörter eine Übersetzung einpflegen?(y/n)")
                if state == "y":
                    word = input("Bitte geben Sie das zu bearbeitende Wort ein: ")
                    language = input("In welcher Sprache möchten Sie die Übersetzung einpflegen? ")
                    if translator.isAuthorized(translator, language):
                        translation = input("Bitte geben Sie die Übersetzung an: ")
                        translator.addTranslation(word, language, translation)
                        print("Ihre Übersetzung wurde erfolgreich eingepflegt.")
                    else:
                        print("Sie sind leider nicht authorisiert für diese Sprache eine Übersetzung einzupflegen. Bitte sprechen Sie mit einem Admin.")
            elif operation == '5':
                print("Sie haben bisher " )
            else:
                print("Auf Wiedersehen!")
                sys.exit()
        else:
            print("Fehlerhafte Eingabe.")