import sys
from admin import Admin
from pattern.singleton import Singleton
from obj.colors import Colors as color

admin = Admin()

class AdminOperator(metaclass=Singleton):

    def operate(self):
        operation = input(color.yellow + "Was möchten Sie tun?(1/2/3/4)\n" + color.end + " 1. Nach einem Wort suchen\n 2. Eine Sprache anlegen\n 3. Einem Übersetzer eine Sprache zuweisen\n 4. Applikation schließen \n" + color.end + " Eingabe: ")
        if operation.isdigit():
            if operation == '1':
                word = input("Bitte geben Sie ein Wort ein: ")
                if word.isalpha():
                    if admin.wordExists(word):
                        translation = admin.showTranslations(word)
                    else:
                        print(color.yellow + "Das eingegebene Wort existiert noch nicht." + color.end)
                else:
                    print(color.red + "Ihre Eingabe war leieder kein valides Wort." + color.end)
            elif operation == '2':
                language = input("Bitte geben Sie eine Sprache an: ")
                if language.isalpha() and len(language.split()) <= 1:
                    language = language.title()
                    admin.addLanguage(language)
                    print(color.green + "Sprache wurde erfolgreich hinzugefügt." + color.end)
                else:
                    print(color.red + "Diese Sprache kann nicht hinzugefügt werden." + color.end)
            elif operation == '3':
                translator = input("Bitte nennen Sie einen Übersetzer per Username: ")
                language = input("Bitte wählen Sie eine registrierte Sprache aus: ")
                if translator.isalnum() and language.isalpha() and len(language.split()) <= 1:
                    admin.assignLanguage(translator, language)
                else:
                    print(color.red + "Sprache kann dem Übersetzer nicht hinzugefügt werden." + color.end)
            else:
                print(color.blue + "Auf Wiedersehen!" + color.end)
                sys.exit()
        else:
            print(color.red + "Fehlerhafte Eingabe." + color.end)
                



