from pathlib import Path
import sys
root = Path(__file__).parent.parent
utilsPath = str(root) + '/folder1'
sys.path.insert(1, utilsPath)
from utils import initAddedLanguagesDBState, initExistentLanguagesDBState, calculateTranslationState
from obj.user import User

class Translator(User):

    def getTranslations(self):
        calculateTranslationState()



