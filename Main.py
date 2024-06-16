from Signup import SignuPage
from Login import LoginPage
from Deposit import DepositPage

class MainPage:
    @staticmethod
    def main_In():        
        print("Welcome to the Banking System")
        print("------------------------------")

        while True:
            print("Are you a new or existing user?")
            print("1. New")
            print("2. Existing")
            try:
                option = int(input("Option: "))
                if option == 1:
                    signup = SignuPage()
                    signup.details()
                    print("\nRedirecting to Login Page...\n")
                    log = LoginPage(SignuPage)
                    log.verification()
                    MainPage.Menu_option()
                elif option == 2:
                    log = LoginPage(SignuPage)
                    log.verification()
                    MainPage.Menu_option()
                else:
                    print("Invalid option. Please enter 1 for New user or 2 for Existing user.")
            except ValueError:
                print("Please Enter a Number Value")

    @staticmethod
    def Menu_option():        
        while True:
            print("Please Select from below options: ")
            print("1.   Deposit")
            print("2.   Withdraw")
            print("3.   Check Balance")
            print("4.   Admin Access")
            try:
                user = int(input("Option: "))
                if user == 1:
                    dep = DepositPage()
                    dep.Deposit_Cash()
                    break
            except ValueError:
                print("Please Enter a Number Value")


MainPage.main_In()
