from pathlib import Path
import sys
root = Path(__file__).parent.parent
utilsPath = str(root) + '/folder1'
sys.path.insert(1, utilsPath)
from design_patterns import Singleton
from utils import getDBData, generate_uuid, saveDBData, initExistentLanguagesDBState


class Admin(metaclass=Singleton):
    
    def addLanguage(self, language):
        dbData = getDBData("languages")
        newLanguageDict = { language: generate_uuid()}
        if language in dbData.keys():
            print("Diese Sprache wurde bereits angelegt.")
        else:
            dbData.update(newLanguageDict)
            saveDBData("languages", dbData)
            initExistentLanguagesDBState()
    
    def wordExists(self, word):
        dbData = getDBData("general")
        words = dbData.keys()
        if word in words:
            return True
        else:
            return False

    def getTranslationsOfWord(self, word):
        dbData = getDBData("general")
        translations = []
        if Admin.wordExists(self, word):
            for k,v in dbData.items():
                if k == word:
                    for d, i in v.items():
                        if d == "translations":
                            for pair in i.items():
                                translations.append(pair)
                                
        return translations

    def showTranslations(self, word):
        translations = Admin.getTranslationsOfWord(self, word)
        if translations is None:
            print("Für dieses Wort wurden bisher keine Übersetzungen eingepflegt.")
        else:
            print("Übersetzungen von dem Wort " + word + " : ")
            for tupel in translations:
                language = tupel[0]
                translation = tupel[1]
                if not translation:
                    translation = "Keine"
                print(language + " - " + translation)

    def assignLanguage(self, translator, language):
        registeredUsersDBData = getDBData("registered")
        languagesDBData = getDBData("languages")
        policiesDBData = getDBData("policies")

        if translator in registeredUsersDBData['translators'] and language in languagesDBData.keys():
            for k,v in policiesDBData.items():
                if k == translator: 
                    authLanguages = v["authLanguages"]
                    if language in authLanguages:
                        print("Dieser Übersetzer darf bereits die eingegebene Sprache verwenden.")
                    else:
                        authLanguages.append(language)
                        saveDBData("policies", policiesDBData)
                        print("Sprache wurde erfolgreich freigegeben!")
        elif translator not in registeredUsersDBData['translators']:
            print("Der genannte User ist nicht registriert.")
        elif language not in languagesDBData.keys():
            print("Die eingegebene Sprache ist noch nicht registriert.")
        else:
            print("AdminError: Please contact the developer")
                    

            

    def say(self):
        print("I'm from another world!")
