from AtmException import DepositeError,WithdrawError,InsuffFundError
Bal=500.00
def Deposite():
    damt= int(input('Enter your Amount to Deposite:'))
    if damt<=0:
        raise DepositeError
    else:
        global Bal
        Bal=Bal+damt
        print('Your Acc. xxxxxxxxxx123 has been credited with INR:{}'.format(damt))
        print('Available Balance in your Ac.xxxxxxxxx123 is INR:{}'.format(Bal))
def Withdraw():
    global Bal
    wamt=int(input('Enter your Amount to Withdraw:'))
    if wamt<=0:
        raise WithdrawError
    elif (wamt+500)>Bal:
        raise InsuffFundError
    else:
        Bal=Bal-wamt
        print('Your Acc. xxxxxxxxxx123 has been debited with INR:{}'.format(wamt))
        print('Available Balance in your Ac.xxxxxxxxx123 is INR:{}'.format(Bal))
def CheckBalance():
    print('Available Balance in your Ac. is INR:{}'.format(Bal))