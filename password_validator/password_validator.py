import re

def execute():
    newPassword = input("Enter you new password: ")
    isValidPassword = validate_password(newPassword)
    if(isValidPassword):
        print("\nIt is a correct password!\n", isValidPassword)
    else:
        print("\nIt is not a correct password!\n", isValidPassword)
    



def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$'
    return bool(re.match(pattern, password))