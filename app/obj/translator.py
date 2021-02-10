from utils import initAddedLanguagesDBState, initExistentLanguagesDBState, calculateTranslationState, getDBData, isRegistered, saveDBData, initExistentLanguagesDBState
from obj.user import User
from obj.colors import Colors as color


class Translator(User):

    def getUncompleteTranslatedWords(self):
        dbData = getDBData("general")
        for word, data in dbData.items():
            if data['translationState'] < 100:
                print(str(word) + " " +str(data['translationState']) + "%")

    def isAuthorized(self, translatorName: str, language: str):
        dbData = getDBData("policies")
        
        try:
            authLanguages = dbData[translatorName]['authLanguages']
            if translatorName in dbData.keys() and language in authLanguages:
                return True
        except:
            print("Der User ist nicht hinterlegt.")
            return False

    def addTranslation(self, word: str, language: str, translation: str):
        dbData = getDBData("general")
        translationDict = { language: translation}
        for k in dbData:
            if word == k:
                translations = dbData[k]['translations']
                for l,t  in translations.items():
                    if l == language:
                        translations.update(translationDict)
        initExistentLanguagesDBState()
        saveDBData("general", dbData)
        calculateTranslationState()

    def getNumberOfTranslatedWords(self, translator: str):
        dbData = getDBData("words")
        for k,v in dbData.items():
            if k == "translatedWords":
                for i,j in v.items():
                    if i == translator:
                        return j

    def updateTranslatorTranslatedWords(self, translator: str):
        wordsDBData = getDBData("words")
        addedWordsDict = wordsDBData['translatedWords']
        addedWordsDict[translator] = addedWordsDict[translator]+1
        
        saveDBData("words", wordsDBData)

    def showNumberOfTranslatedWords(self, translator: str):
        print(color.green + "Anzahl hinzugefügter Wörter: " + color.end  + color.underline + str(Translator.getNumberOfTranslatedWords(self, translator)) + color.end)


                        
                
        


            
        





