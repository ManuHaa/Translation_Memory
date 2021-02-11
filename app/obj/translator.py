from obj.utils import Utils as util
from obj.user import User
from obj.colors import Colors as color


class Translator(User):

    def checkIfWortExists(self, word):
        dbData = util.getDBData("general")
        words = []
        for key in dbData.keys():
            words.append(key)
        if word in words:
            return True
        else:
            return False

    def getUncompleteTranslatedWords(self):
        dbData = util.getDBData("general")
        for word, data in dbData.items():
            if data['translationState'] < 100:
                print(str(word) + " " +str(data['translationState']) + "%")

    def isAuthorized(self, translatorName: str, language: str):
        dbData = util.getDBData("policies")
        
        try:
            authLanguages = dbData[translatorName]['authLanguages']
            if translatorName in dbData.keys() and language in authLanguages:
                return True
        except:
            print("Der User ist nicht hinterlegt.")
            return False

    def addTranslation(self, word: str, language: str, translation: str):
        dbData = util.getDBData("general")
        translationDict = { language: translation}
        for k in dbData:
            if word == k:
                translations = dbData[k]['translations']
                for l,t  in translations.items():
                    if l == language:
                        translations.update(translationDict)
        util.initExistentLanguagesDBState()
        util.saveDBData("general", dbData)
        util.calculateTranslationState(word)

    def getNumberOfTranslatedWords(self, translator: str):
        dbData = util.getDBData("words")
        for k,v in dbData.items():
            if k == "translatedWords":
                for i,j in v.items():
                    if i == translator:
                        return j

    def updateTranslatorTranslatedWords(self, translator: str):
        wordsDBData = util.getDBData("words")
        addedWordsDict = wordsDBData['translatedWords']
        addedWordsDict[translator] = addedWordsDict[translator]+1
        
        util.saveDBData("words", wordsDBData)

    def showNumberOfTranslatedWords(self, translator: str):
        print(color.green + "Anzahl übersertzter Wörter: " + color.end  + color.underline + str(Translator.getNumberOfTranslatedWords(self, translator)) + color.end)


                        
                
        


            
        





