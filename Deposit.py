#Deposit Page
class Deposit:

    def __init__(self):
        self.balance = 0

    print("Welcome to Deposit Page")
    print("---------------------------")


    def Deposit_Cash(self):
        while(True):
            deposit_amount = input("Please Enter Amount: ")
            
            if(deposit_amount.isdigit()):
                deposit_amount = float(deposit_amount)
                if(deposit_amount > 0):

                    self.balance += deposit_amount
                    print(f'Your total amount to be deposited is ${deposit_amount}')
                    print(f"New balance is ${self.balance}")
                    break
                else:
                    print("Please enter value in postive integer again")
            else:
                print("Please Enter a number value")
deposit_page = Deposit()
deposit_page.Deposit_Cash()