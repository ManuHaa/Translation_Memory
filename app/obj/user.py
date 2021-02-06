from pathlib import Path
import sys
root = Path(__file__).parent.parent
utilsPath = str(root) + '/folder1'
sys.path.insert(1, utilsPath)
from utils import getDBData, generate_uuid, saveDBData


class User:
    
    #def __init__(self, addedWords):
        #self._addedWords = addedWords

    def addWord(self, word):
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
        print(dbData)
        saveDBData("general", dbData)

    def getNumberOfRegisteredWords(self):
        dbData = getDBData("general")
        for k, v in dbData.items():
            return len(v)

    def showNumberOfRegisteredWords(self):
        print("Anzahl registrierter Wörter: " + str(User.getNumberOfRegisteredWords(self)))
            

    def getNumberOfCompleteTranslatedWords(self):
        pass

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
        if User.wordExists(self, word):
            for k,v in dbData.items():
                if k == word:
                    for d, i in v.items():
                        if d == "translations":
                            for pair in i.items():
                                translations.append(pair)
                                
        return translations

    def showTranslations(self, word):
        translations = User.getTranslationsOfWord(self, word)
        
        print("Übersetzungen von dem Wort " + word + " : ")
        for tupel in translations:
            language = tupel[0]
            translation = tupel[1]
            if not translation:
                translation = "Keine"
            print(language + " - " + translation)
        
            

    def say(self):
        print("I'm from another world!")

    def getNumberOfAddedWords(self):
        dbData = getDBData("words")
        for k,v in dbData.items():
            if k == "addedWords":
                for i,j in v.items():
                    if i =="user":
                        return j

    def showNumberOfAddedWords(self):
        print("Anzahl hinzugefügter Wörter: " + str(User.getNumberOfAddedWords(self)))

                
