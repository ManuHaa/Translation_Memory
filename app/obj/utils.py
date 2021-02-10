import os
import json
import uuid
import array

class Utils:
    #-base vars
    uuids = []
    path = os.getcwd()
    basePath = os.path.abspath(os.path.join('/database', path))
    # basePath = os.path.dirname(os.path.abspath(__file__))

    #-returns already generated 
    def get_used_uuids() -> list:
        return Utils.uuids

    #-adds an id to uuid storage
    def add_uuid(id: str):
        Utils.get_used_uuids().append(id)

    #-generates an individual uuid
    def generate_uuid():
        id = str(uuid.uuid4())
        if id in Utils.get_used_uuids():
            return Utils.generate_uuid()
        Utils.add_uuid(id)
        return id


    #-returns path of required DB file
    def getDBPath(dbName: str):
        if dbName == "general":
            return Utils.basePath + "/database/generalDB.json"
        elif dbName == "languages":
            return Utils.basePath + "/database/languagesDB.json"
        elif dbName == "registered":
            return Utils.basePath + "/database/registeredUsersDB.json"
        elif dbName == "words":
            return Utils.basePath + "/database/wordsDB.json"
        else:
            return Utils.basePath + "/database/policiesDB.json"

    #-returns data of reuired DB as dict
    def getDBData(dbName: str):
        dbFile = open(Utils.getDBPath(dbName), "r")
        dbData = json.load(dbFile)
        dbFile.close()

        return dbData

    #-overwrites DB data
    def saveDBData(dbName: str, dictData: dict):
        dbFile = open(Utils.getDBPath(dbName), "w")
        dbFile.write(json.dumps(dictData, indent=4, sort_keys=True))
        dbFile.close()

    #-returns number of added words (user)
    def getNumberOfAddedWords():
        dbFile = open(Utils.getDBPath("user"), "r")
        dbData = json.load(dbFile)
        dbFile.close()

        return dbData['addedWords']

    #-returns Number of all words from words DB
    def getNumberOfRegisteredWords():
        dbFile = open(Utils.getDBPath("words"), "r")
        dbData = json.load(dbFile)
        dbFile.close()
            
        return len(dbData['words'])

    #-initializes the language and general DB if languages added manually
    def initAddedLanguagesDBState():
        languages = Utils.getDBData("languages").keys()
        generalDBData = Utils.getDBData("general")

        for words, data in generalDBData.items():
            translationDict = data["translations"]
            print(translationDict)
            if not translationDict:
                for language in languages:
                    temp = { language: "Keine"}
                    translationDict.update(temp)
        Utils.saveDBData("general", generalDBData)

    #-initializes the language and general DB of existent languages and translations
    def initExistentLanguagesDBState():
        languages = Utils.getDBData("languages").keys()
        generalDBData = Utils.getDBData("general")

        for words, data in generalDBData.items():
            translationDict = data["translations"]
            for language in languages:
                if language not in translationDict.keys():
                    temp = { language: "Keine"}
                    translationDict.update(temp)
        Utils.saveDBData("general", generalDBData)

    #-calculates the translation state of every word from general DB
    def calculateTranslationState(word):
        generalDBData = Utils.getDBData("general")
        translationState = generalDBData[word]['translationState']
        translations = generalDBData[word]['translations']

        numberLanguages = len(translations.keys())
        noneObjects = []
        for value in translations.values():
            if value == "Keine":
                noneObjects.append(value)
        numberNoneObjects = len(noneObjects)
        numberTranslations = numberLanguages - numberNoneObjects
        generalDBData[word]['translationState'] = int((numberTranslations/numberLanguages) * 100)
        Utils.saveDBData("general", generalDBData)

    def initTranslationStates():
        generalDBData = Utils.getDBData("general")
        for word in generalDBData:
            Utils.calculateTranslationState(word)
        
            

    #-checks if the given dict contains the given key value pair
    def checkIfPairInDict(key: str, value: str, dictionary: dict):
        if key in dictionary and value == dictionary[key]:
            return True
        else:
            return False