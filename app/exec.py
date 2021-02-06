
from login.authentication import Atuhtenticator
from login.login import LoginMask
from operators.userOperator import UserOperator
auth = Atuhtenticator()
login = LoginMask()
user = UserOperator()

loopState = True

while(loopState == True):
    
    if login.loginMaskOperator()['operator'] == "user":
        user.operate()
        