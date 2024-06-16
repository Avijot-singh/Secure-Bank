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
            elif email in Signup.emails:
                print("This email is already in use. Please login or use another email.")
            else:
                Signup.emails.append(email)
                return email
    
    
    def details(self):
        print("First Name:", self.Fname)
        print("Last Name:", self.Lname)
        print("Date Of Birth:", self.DOB)
        print("Email:", self.Email)

# Create an instance of Signup to test the input
new_signup = SignuPage()
new_signup.details()