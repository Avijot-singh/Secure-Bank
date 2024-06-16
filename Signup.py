import datetime
import re

class SignuPage:
    emails = []
    account_number = 11001101
    
    def __init__(self):
        self.Fname = self.get_name("first")
        self.Lname = self.get_name("last")
        self.DOB = self.get_dob()
        self.Email = self.get_email()
        self.password = self.password_check()
        self.account_number = Signup.account_number
        Signup.account_number += 1

    def get_name(self, name_type):
        while True:
            name = input(f"Please Enter Your {name_type.capitalize()} Name:  ")
            if name.isalpha():
                return name
            else:
                print(f"Invalid {name_type} name. Please enter only letters.")

    def get_dob(self):
        while True:
            dob = input("Please Enter Your Date Of Birth in DD/MM/YYYY format:   ")
            try:
                datetime.datetime.strptime(dob, "%d/%m/%Y")
                return dob
            except ValueError:
                print("Invalid date format. Please enter the date in DD/MM/YYYY format.")

    def get_email(self):
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        while True:
            email = input("Please Enter your Email:  ")
            if not re.match(email_pattern, email):
                print("Invalid email format. Please enter a valid email address.")
            elif email in SignuPage.emails:
                print("This email is already in use. Please login or use another email.")
            else:
                SignuPage.emails.append(email)
                return email
    
    
    def password_check(self):
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,10}$" # reg is the regex pattern used for validation of the password using the set conditions
        pat = re.compile(reg) #Compiles the regex pattern into a regex object for better performance.
        while True:
            password = input("Please enter the Password you want to set:(1 UPPERCASE, 1 lowercase, 1 digit and a special character, min 6 and max 10)")
            mat = re.search(pat, password) #Searches the password for a match to the compiled regex pattern pat.
            if mat:
                print("Password Set")
                return password
            else:
                print("Invalid Password")

            
    def details(self):
        print("Hey, ", self.Fname, self.Lname, "Your Account has been set up and your Account Number is :", self.account_number, ", Next time please use your email and password to login into your account.")

# Create an instance of Signup to test the input
new_signup1 = Signup()
new_signup1.details()




    