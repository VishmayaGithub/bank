i = ''
amount = 20000
class Atm(object):
    
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber
        

    def withdraw(self):
        i = int(input('Enter Amount to withdraw in number only'))  
        if(i>10000):
            print('Amount exeeded limit')
        if(i<10000):
            print('You have withdrawn ',i,'successfully. The amount remaining in you account is Rupees ',amount-i)    
    def add_money(self):
        add = int(input('Enter amount to deposit into your bank account'))
        if(add>10000):
            print('Amount exeeded limit')
        if(add<10000):
            print('You have added ',add,'to your bank account. You account balance is',amount+add)
def main():
    num = input('Enter card number')
    pin = input('Enter pin number')
    user = Atm(num,pin)
    print('Do you want to : 1.Withdraw 2.Deposit. Enter your option number below')
    choose= int(input('Enter 1 or 2'))
    if(choose==1):
        user.withdraw()
    elif(choose==2):
        user.add_money()
    else:
        print('Enter correct option ~_~')        

main()       