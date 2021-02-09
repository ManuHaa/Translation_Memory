
from login.authentication import Atuhtenticator
from login.login import LoginMask
from operators.userOperator import UserOperator
from operators.adminOperator import AdminOperator
from operators.translatorOperator import TranslatorOperator
auth = Atuhtenticator()
login = LoginMask()
user = UserOperator()
admin = AdminOperator()
translator = TranslatorOperator()

loopState = True

#while(loopState == True):
    
    #if login.loginMaskOperator()['operator'] == "user":
        #user.operate()
    #elif login.loginMaskOperator()['operator'] == "admin":
        #admin.operate()
authenticatedPerson = None
operator = login.loginMaskOperator()['operator']

while(loopState == True):
    if operator == "translator":
        translator.operate()
    elif operator == "admin":
        admin.operate()
    else:
        user.operate()

