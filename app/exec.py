
from login.login import LoginMask
from operators.userOperator import UserOperator
from operators.adminOperator import AdminOperator
from operators.translatorOperator import TranslatorOperator


login = LoginMask()
user = UserOperator()
admin = AdminOperator()
translator = TranslatorOperator()

loopState = True

operator = login.loginMaskOperator()['operator']

while(loopState == True):
    if operator == "translator":
        translator.operate()
    elif operator == "admin":
        admin.operate()
    else:
        user.operate()

