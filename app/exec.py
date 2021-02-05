
from authentication import Atuhtenticator
from login import LoginMask
from userOperator import UserOperator
auth = Atuhtenticator()
login = LoginMask()
user = UserOperator()

loopState = True

while(loopState == True):
    
    if login.loginMaskOperator()['operator'] == "user":
        user.operate()
        