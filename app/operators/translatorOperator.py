import sys
from translator import Translator
from pattern.singleton import Singleton
from obj.colors import Colors as color

translator = Translator()

class TranslatorOperator(metaclass=Singleton):
    def operate(self):
        operation = input(color.yellow + "Was möchten Sie tun?(1/2/3/4/5/6)\n" + color.end + " 1. Nach einem Wort suchen\n 2. Anzahl angelegter Wörter anzeigen\n 3. Alle registrierten Wörter anzeigen lassen\n 4. Unkomplette Übersetzungen auflisten lassen\n 5. Anzahl eigener Übersetzungen anzeigen lassen\n 6. Applikation schließen \n" + color.yellow + " Eingabe: " + color.end)
        if operation.isdigit():
            if operation == '1':
                word = input("Bitte geben Sie ein Wort ein: ")
                if word.isalpha():
                    if translator.wordExists(word):
                        translation = translator.showTranslations(word)
                    else:
                        state = input(color.yellow + "Das eingegebene Wort existiert noch nicht. Wollen Sie es anlegen?(y/n)" + color.end)
                        if state == 'y':
                            translator.addWord(word)
                            print(color.green + "Das Wort wurde erfolgreich hinzugefügt!" + color.end)
                else:
                    print(color.red + "Ihre EIngabe war leider kein valides Wort." + color.end)
            elif operation == '2':
                username = input("Bitte geben sie Ihren Username an: ")
                if translator.getNumberOfAddedWords(username) is None:
                    print(color.red + "Sie haben bisher noch keine Wörter angelegt oder den Username falsch eingetragen." + color.end)
                else:
                    translator.showNumberOfAddedWords(username)
            elif operation == '3':
                translator.showNumberOfRegisteredWords()
            elif operation == '4':
                translator.getUncompleteTranslatedWords()
                state = input(color.yellow + "Wollen Sie zu einem dieser Wörter eine Übersetzung einpflegen?(y/n)\n " + color.end +"Eingabe: ")
                if state == 'y':
                    word = input("Bitte geben Sie das zu bearbeitende Wort ein: ")
                    language = input("In welcher Sprache möchten Sie die Übersetzung einpflegen? ")
                    currentUser = input("Bitte geben Sie erneut Ihren Username ein: ")
                    if translator.isAuthorized(currentUser, language):
                        translation = input(color.yellow + "Bitte geben Sie die Übersetzung an: " + color.end)
                        translator.addTranslation(word, language, translation)
                        translator.updateTranslatorTranslatedWords(currentUser)
                        print(color.green + "Ihre Übersetzung wurde erfolgreich eingepflegt." + color.end)
                    else:
                        print(color.red + "Sie sind leider nicht authorisiert für diese Sprache eine Übersetzung einzupflegen. Bitte sprechen Sie mit einem Admin." + color.end)
            elif operation == '5':
                username = input("Bitte geben Sie ihren Username ein: ")
                if translator.getNumberOfTranslatedWords(username) is None:
                    print(color.red + "Sie haben Ihren Username falsch eingegeben oder der Übersetzer existiert nicht." + color.end)
                else:
                    translator.showNumberOfTranslatedWords(username)                
            else:
                print(color.blue + "Auf Wiedersehen!" + color.end)
                sys.exit()
        else:
            print(color.red + "Fehlerhafte Eingabe." + color.end)