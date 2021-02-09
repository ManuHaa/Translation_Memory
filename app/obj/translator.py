from pathlib import Path
import sys
root = Path(__file__).parent.parent
utilsPath = str(root) + '/folder1'
sys.path.insert(1, utilsPath)
from utils import initAddedLanguagesDBState, initExistentLanguagesDBState, calculateTranslationState, getDBData, isRegistered, saveDBData, initExistentLanguagesDBState
from obj.user import User


class Translator(User):

    def getUncompleteTranslatedWords(self):
        dbData = getDBData("general")
        for word, data in dbData.items():
            if data['translationState'] < 100:
                print(str(word) + " " +str(data['translationState']) + "%")

    def isAuthorized(self, translatorName, language):
        dbData = getDBData("policies")
        
        try:
            authLanguages = dbData[translatorName]['authLanguages']
            if translatorName in dbData.keys() and language in authLanguages:
                return True
        except:
            print("Der User ist nicht hinterlegt.")
            return False

    def addTranslation(self, word, language, translation):
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

                        
                
        


            
        





