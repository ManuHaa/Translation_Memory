from obj.user import User

class Translator(User):

    def __init__(self, username, password, translatedWords, authorizedLanguages):
        self.username = username
        self.password = password
        self.translatedWords = translatedWords
        self.authorizedLanguages = authorizedLanguages

    def addTranslation(self):
        pass

    def getNumberOfTranslatedWords(self):
        pass

    def getUncompletedWords(self):
        pass