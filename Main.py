from Deposit import DepositPage # Syntax | from FileName import classname
from Login import LoginPage
class MainPage:
    @staticmethod
    def main_In():        
        print("Welcome to the Banking System")
        print("------------------------------")

        while(True):
            print("Are you a new or existing user?")
            print("1.New")
            print("2.Existing")
            try:
                option = int(input("Option: "))
                if(option == 1):
                    log = LoginPage()
                    log.verification()
                    MainPage.Menu_option()

                # Please add signup here        
            except ValueError:
                print("Please Enter a Number Value")
                
    @staticmethod
    def Menu_option():        
        while(True):
            print("Please Select from below options: ")
            print("1.   Deposit")
            print("2.   Withdraw")
            print("3.   Check Balance")
            print("4.   Admin Access")
            try:
                user = int(input("Option: "))
                if(user == 1):
                    dep = DepositPage()
                    dep.Deposit_Cash()
                    break
            except ValueError:
                print("Please Enter a Number Value")
                

MainPage.main_In()