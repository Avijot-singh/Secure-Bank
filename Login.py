from Signup import SignuPage

class LoginPage:
    def __init__(self, signup_class):
        self.signup_class = signup_class
        print("Login Page")
        print("-------------")

    def verification(self):
        user_name = input("Enter Email: ")
        if user_name in self.signup_class.emails:
            print("Password Verification to be completed")
            
        else:
            print("Email does not exist. Please signup first or try another email.")
