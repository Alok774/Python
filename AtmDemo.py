from AtmMenu import menu
from AtmOperation import Deposite,Withdraw,CheckBalance
from AtmException import DepositeError,WithdrawError,InsuffFundError
while(True):
    menu()
    try:
        ch=int(input('Enter your Choice: '))
        match(ch):
                case 1:
                    try:
                        Deposite()
                    except (ValueError,DepositeError):
                        print('Dont enter Alphanum,str,symbol')
                        print('Dont enter -ve number or Zero values' )
                case 2:
                    try:
                        Withdraw()
                    except (ValueError,WithdrawError):
                        print('Dont enter Alphanum,str,symbol')
                        print('Dont enter -ve number or Zero values' )
                    except InsuffFundError:
                        print('InsufficientBalance in your account')
                case 3:
                    CheckBalance()
                case 4:
                    print('Thanks for using')
                    break
                case _:
                    print('Wrong selection-Try Again')
    except ValueError:
        print('Not enter AphaNumeric,Str,symbol')
