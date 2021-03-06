import sys
from translator import Translator
from pattern.singleton import Singleton
from obj.colors import Colors as color
from operators.loginOperator import LoginMask

login = LoginMask()
translator = Translator()

class TranslatorOperator(metaclass=Singleton):
    def operate(self):
        operation = input(color.yellow + "Was möchten Sie tun?(1/2/3/4/5/6)\n" + color.end + " 1. Nach einem Wort suchen\n 2. Anzahl angelegter Wörter anzeigen\n 3. Anzahl aller registrierter Wörter anzeigen mit Anzahl komplett übersetzer Wörter\n 4. Unkomplette Übersetzungen auflisten\n 5. Anzahl selbst übersetzter Wörter anzeigen\n 6. Applikation schließen \n" + color.yellow + " Eingabe: " + color.end)
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
                            translator.updateAddedWords(login.currentUser['username'])
                            print(color.green + "Das Wort wurde erfolgreich hinzugefügt!" + color.end)
                else:
                    print(color.red + "Ihre EIngabe war leider kein valides Wort." + color.end)
            elif operation == '2':
                if translator.getNumberOfAddedWords(login.currentUser['username']) is None:
                    print(color.red + "Sie haben bisher noch keine Wörter angelegt oder den Username falsch eingetragen." + color.end)
                else:
                    translator.showNumberOfAddedWords(login.currentUser['username'])
            elif operation == '3':
                translator.showNumberOfRegisteredWords()
            elif operation == '4':
                translator.getUncompleteTranslatedWords()
                state = input(color.yellow + "Wollen Sie zu einem dieser Wörter eine Übersetzung einpflegen?(y/n)\n" + color.end +"Eingabe: ")
                if state == 'y':
                    word = input("Bitte geben Sie das zu bearbeitende Wort ein: ")
                    if translator.checkIfWortExists(word):
                        language = input("In welcher Sprache möchten Sie die Übersetzung einpflegen? ")
                        if word.isalpha() and len(word.split()) == 1 and language.isalpha() and len(language.split()) == 1:
                            language = language.title()
                            if translator.isAuthorized(login.currentUser['username'], language):
                                translation = input(color.yellow + "Bitte geben Sie die Übersetzung an: " + color.end)
                                translator.addTranslation(word, language, translation)
                                translator.updateTranslatorTranslatedWords(login.currentUser['username'])
                                print(color.green + "Ihre Übersetzung wurde erfolgreich eingepflegt." + color.end)
                            else:
                                print(color.red + "Sie sind leider nicht authorisiert für diese Sprache eine Übersetzung einzupflegen. Bitte sprechen Sie mit einem Admin." + color.end)
                        else:
                            print(color.red + "Ihre Eingaben für Wort und Sprache waren nicht valide." + color.end)
                    else:
                        print(color.red + "Das von Ihnen eingegebene Wort existiert nicht in der Datenbank" +  color.end)
                elif state == 'n':
                    pass
                else:
                    print(color.red + "Keine valide Eingabe" + color.end)
            elif operation == '5':
                if translator.getNumberOfTranslatedWords(login.currentUser['username']) is None:
                    print(color.red + "Sie haben Ihren Username falsch eingegeben oder der Übersetzer existiert nicht." + color.end)
                else:
                    translator.showNumberOfTranslatedWords(login.currentUser['username'])                
            else:
                print(color.blue + "Auf Wiedersehen!" + color.end)
                sys.exit()
        else:
            print(color.red + "Fehlerhafte Eingabe." + color.end)