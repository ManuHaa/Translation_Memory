import sys
import os
from pathlib import Path
root = Path(__file__).parent.parent
objPath = str(root) + '/obj'
sys.path.insert(1, objPath)
from user import User

#from obj.admin import Admin
#from login import Atuhtenticator
#from obj.user import User

user = User()

user.showTranslations("Hallo")




