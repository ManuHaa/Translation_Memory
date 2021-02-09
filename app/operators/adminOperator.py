from admin import Admin
from pattern.singleton import Singleton

admin = Admin()

class AdminOperator(metaclass=Singleton):

    def operate(self):
        operation = input("Was möchten Sie tun?(1/2/3/4)\n 1. Nach einem Wort suchen\n 2. Eine Sprache anlegen\n 3. Einem Übersetzer eine Sprache zuweisen\n 4. Applikation schließen \n Eingabe: ")
        if operation.isdigit():
            if operation == "1":
                word = input("Bitte geben Sie ein Wort ein: ")
                if word.isalpha():
                    if admin.wordExists(word):
                        translation = admin.showTranslations(word)
                    else:
                        print("Das eingegebene Wort existiert noch nicht.")
                else:
                    print("Ihre Eingabe war leieder kein valides Wort.")
            elif operation == "2":
                language = input("Bitte geben Sie eine Sprache an: ")
                if language.isalpha() and len(language.split()) <= 1:
                    language = language.title()
                    admin.addLanguage(language)
                    print("Sprache wurde erfolgreich hinzugefügt.")
                else:
                    print("Diese Sprache kann nicht hinzugefügt werden.")
            elif operation == "3":
                translator = input("Bitte nennen Sie einen Übersetzer per Username: ")
                language = input("Bitte wählen Sie eine registrierte Sprache aus: ")
                if translator.isalnum() and language.isalpha() and len(language.split()) <= 1:
                    admin.assignLanguage(translator, language)
                else:
                    print("Sprache kann dem Übersetzer nicht hinzugefügt werden.")
            else:
                print("Auf Wiedersehen!")
                sys.exit()
        else:
            print("Fehlerhafte Eingabe.")
                



