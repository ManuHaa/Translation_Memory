from utils import getDBData, checkIfPairInDict

class Atuhtenticator:
    
    def isTranslator(self, username: str, password: str):
        dbData = getDBData("registered")
        key, val = username, password

        if checkIfPairInDict(key, val, dbData["translators"]):
            return True
        else:
            return False

    def isAdmin(self, username: str, password: str):
        dbData = getDBData("registered")
        key, val = username, password

        if checkIfPairInDict(key, val, dbData["admins"]):
            return True
        else:
            return False

    def isRegistered(self, username: str, password: str):
        dbData = getDBData("registered")
        translators = dbData["translators"]
        admins = dbData["admins"]
        key, val = username, password

        if checkIfPairInDict(key, val, admins) or checkIfPairInDict(key, val, translators):
            print("yes")









