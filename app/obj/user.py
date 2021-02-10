from utils import getDBData, generate_uuid, saveDBData, initAddedLanguagesDBState, initExistentLanguagesDBState
from pattern.singleton import Singleton
from pattern.null_object import Null
from utils import Colors as color

class User(metaclass=Singleton):

    def addWord(self, word: str):
        dbData = getDBData("general")
        wordDict = {
            word: {
                "id": generate_uuid(),
                "translationState": 0,
                "translations": {

                }
            }
        }
        dbData.update(wordDict)
        saveDBData("general", dbData)
        initExistentLanguagesDBState()

    def updateUserAddedWords(self):
        wordsDBData = getDBData("words")
        addedWordsDict = wordsDBData['addedWords']
        addedWordsDict['user'] = addedWordsDict['user']+1
        
        saveDBData("words", wordsDBData)

    def getNumberOfRegisteredWords(self):
        dbData = getDBData("general")
        return len(dbData)
            
    def getNumberOfCompleteTranslatedWords(self):
        dbData = getDBData("general")
        arr = []
        for word, data in dbData.items():
            translationState = data['translationState']
            if translationState == 100:
                arr.append(translationState)
        return len(arr)

    def wordExists(self, word: str):
        dbData = getDBData("general")
        words = dbData.keys()
        if word in words:
            return True
        else:
            return False

    def getTranslationsOfWord(self, word: str):
        dbData = getDBData("general")
        translations = []
        if User.wordExists(self, word):
            for k,v in dbData.items():
                if k == word:
                    for d, i in v.items():
                        if d == "translations":
                            for pair in i.items():
                                translations.append(pair)
                                
        return translations

    def getNumberOfAddedWords(self, operator: str):
        dbData = getDBData("words")
        for k,v in dbData.items():
            if k == "addedWords":
                for i,j in v.items():
                    if i == operator:
                        return j
                else:
                    return Null()

    def showNumberOfAddedWords(self, operator: str):
        print(color.green + "Anzahl hinzugefügter Wörter: " + color.end + color.underline + str(User.getNumberOfAddedWords(self, operator)) + color.end)

    def showNumberOfRegisteredWords(self):
        print(color.green + "Anzahl registrierter Wörter: " + color.end + color.underline + str(User.getNumberOfRegisteredWords(self))+ color.end + color.green + "\nDavon ist/sind " + color.end + color.underline + str(User.getNumberOfCompleteTranslatedWords(self)) + color.end + color.green + " Wort/Wörter komplett übersetzt." + color.end)

    def showTranslations(self, word: str):
        translations = User.getTranslationsOfWord(self, word)
        
        print(color.green + "Übersetzungen von dem Wort " + color.end + color.underline + word + color.end +" : ")
        for tupel in translations:
            language = tupel[0]
            translation = tupel[1]
            if not translation:
                translation = "Keine"
            print(language + " - " + translation)