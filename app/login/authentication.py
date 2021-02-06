from utils import getDBData, checkIfPairInDict

class Atuhtenticator:
    
    def isTranslator(self, username, password):
        dbData = getDBData("registered")
        key, val = username, password

        if checkIfPairInDict(key, val, dbData["translators"]):
            print("yes")
            return True
        else:
            return False

    def isAdmin(self, username, password):
        dbData = getDBData("registered")
        key, val = username, password

        if checkIfPairInDict(key, val, dbData["admins"]):
            print("yes")
            return True
        else:
            return False

    def isRegistered(self, username, password):
        dbData = getDBData("registered")
        translators = dbData["translators"]
        admins = dbData["admins"]
        key, val = username, password

        if checkIfPairInDict(key, val, admins) or checkIfPairInDict(key, val, translators):
            print("yes")









