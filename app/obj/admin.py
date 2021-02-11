from pattern.singleton import Singleton
from obj.utils import Utils as util
from obj.colors import Colors as color


class Admin(metaclass=Singleton):

    def wordExists(self, word: str):
        dbData = util.getDBData("general")
        words = dbData.keys()
        if word in words:
            return True
        else:
            return False

    def getTranslationsOfWord(self, word: str):
        dbData = util.getDBData("general")
        translations = []
        if Admin.wordExists(self, word):
            for k,v in dbData.items():
                if k == word:
                    for d, i in v.items():
                        if d == "translations":
                            for pair in i.items():
                                translations.append(pair)
                                
        return translations
    
    def addLanguage(self, language: str):
        dbData = util.getDBData("languages")
        newLanguageDict = { language: util.generate_uuid()}
        if language in dbData.keys():
            print("Diese Sprache wurde bereits angelegt.")
        else:
            dbData.update(newLanguageDict)
            util.saveDBData("languages", dbData)
            util.initExistentLanguagesDBState()
            util.initTranslationStates()

    def assignLanguage(self, translator: str, language: str):
        registeredUsersDBData = util.getDBData("registered")
        languagesDBData = util.getDBData("languages")
        policiesDBData = util.getDBData("policies")

        if translator in registeredUsersDBData['translators'] and language in languagesDBData.keys():
            for k,v in policiesDBData.items():
                if k == translator: 
                    authLanguages = v["authLanguages"]
                    if language in authLanguages:
                        print(color.yellow + "Dieser Übersetzer darf bereits die eingegebene Sprache verwenden." + color.end)
                    else:
                        authLanguages.append(language)
                        util.saveDBData("policies", policiesDBData)
                        print(color.green + "Sprache wurde erfolgreich freigegeben!" + color.end)
        elif translator not in registeredUsersDBData['translators']:
            print(color.red + "Der genannte User ist nicht registriert." + color.end)
        elif language not in languagesDBData.keys():
            print(color.red + "Die eingegebene Sprache ist noch nicht registriert." + color.end)
        else:
            print(color.red + "AdminError: Please contact the developer" + color.end)

    def showTranslations(self, word: str):
        translations = Admin.getTranslationsOfWord(self, word)
        if translations is None:
            print(color.yellow + "Für dieses Wort wurden bisher keine Übersetzungen eingepflegt." + color.end)
        else:
            print(color.green + "Übersetzungen von dem Wort " + color.end + color.underline + word + color.end + color.green + " : " + color.end)
            for tupel in translations:
                language = tupel[0]
                translation = tupel[1]
                if not translation:
                    translation = "Keine"
                print(language + " - " + translation)
