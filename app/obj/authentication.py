from obj.utils import Utils as util

class Atuhtenticator:
    
    def isTranslator(self, username: str, password: str):
        dbData = util.getDBData("registered")
        key, val = username, password

        if util.checkIfPairInDict(key, val, dbData["translators"]):
            return True
        else:
            return False

    def isAdmin(self, username: str, password: str):
        dbData = util.getDBData("registered")
        key, val = username, password

        if util.checkIfPairInDict(key, val, dbData["admins"]):
            return True
        else:
            return False

    def isRegistered(self, username: str, password: str):
        dbData = util.getDBData("registered")
        translators = dbData["translators"]
        admins = dbData["admins"]
        key, val = username, password

        if checkIfPairInDict(key, val, admins) or checkIfPairInDict(key, val, translators):
            print("yes")









