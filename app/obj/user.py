
import json
import array
import os
from utils import getDBPath, generate_uuid, getNumberOfAddedWords,getNumberOfRegisteredWords, getDBData


        
class User:
        
    def addWord(self, word):
        newWord = {
            word:generate_uuid()
        }
        dBData = getDBData("words")
        
        wordsArr = dbData['words']
        for obj in wordsArr:
                for k,v in obj.items():
                    if k == word:
                        exists = True
                    else:
                        exists = False
                        
        if exists == False:
            wordsArr.append(newWord)
            dbFile = open(getDBPath("words"), "w")
            dbFile.write(json.dumps(dbData, indent=4, sort_keys=True))
            dbFile.close()
            print("Das Wort wurde hinzugefügt.")

            dbFile = open(getDBPath("user"), "r")
            dbData = json.load(dbFile)
            dbFile.close()

            dbData['addedWords'] = dbData['addedWords'] + 1

            dbFile = open(getDBPath("user"), "w")
            dbFile.write(json.dumps(dbData, indent=4, sort_keys=True))
            dbFile.close()

            return True
            
        else:
            print("Das eingegebene Wort existiert bereits.")
            return False        

    def showNumberOfAddedWords(self):
        print("Hinzugefügte Worte: " + str(getNumberOfAddedWords()))

    def showNumberOfRegisteredWords(self):
        print("Alle registrierten Worte: " + str(getNumberOfRegisteredWords()))

    def getNumberOfCompleteTranslatedWords(self):
        pass

    def searchWord(self, word:str):
        dbData = getDBData("words")
        
        wordsArr = dbData['words']

        for obj in wordsArr:
            if word in obj:
                print(word)
            else:
                print("no")


        
        








