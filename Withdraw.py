#Withdraw Page
class WithdrawPage:

    def __init__(self):
        self.balance = 0
        print("Welcome to Withdraw Page")
        print("---------------------------")


    def Withdraw_Cash(self):
        while(True):
            Withdraw_amount = input("Please Enter Amount: ")
            
            if(Withdraw_amount.isdigit()):
                Withdraw_amount = float(Withdraw_amount)
                if(Withdraw_amount > self.balance):
                    print("You do not have enough credit in your account")
                else:
                    self.balance -= Withdraw_amount
                    print(f'Your total amount to be Withdrawn is ${Withdraw_amount}')
                    print(f"New balance is ${self.balance}")
                    break
            else:
                print("Please Enter only numbers")
