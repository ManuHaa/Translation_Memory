
from login.authentication import Atuhtenticator
from login.login import LoginMask
from operators.userOperator import UserOperator
from operators.adminOperator import AdminOperator
auth = Atuhtenticator()
login = LoginMask()
user = UserOperator()
admin = AdminOperator()

loopState = True

#while(loopState == True):
    
    #if login.loginMaskOperator()['operator'] == "user":
        #user.operate()
    #elif login.loginMaskOperator()['operator'] == "admin":
        #admin.operate()
authenticatedPerson = None
operator = login.loginMaskOperator()['operator']
if operator == "user":
    user.operate()
elif operator == "admin":
    admin.operate()

        