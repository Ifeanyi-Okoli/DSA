"""  
Your job is to create a simple password validation function, as seen on many websites.

The rules for a valid password are as follows:

There needs to be at least 1 uppercase letter.
There needs to be at least 1 lowercase letter.
There needs to be at least 1 number.
The password needs to be at least 8 characters long.
You are permitted to use any methods to validate the password.

Examples:
password("Abcd1234"); ===> true
password("Abcd123"); ===> false
password("abcd1234"); ===> false
password("AbcdefGhijKlmnopQRsTuvwxyZ1234567890"); ===> true
password("ABCD1234"); ===> false
password("Ab1!@#$%^&*()-_+={}[]|\:;?/>.<,"); ===> true;
password("!@#$%^&*()-_+={}[]|\:;?/>.<,"); ===> false;
"""
import re
def password(string):
    #your code here
    # return (any(i.isupper() for i in string) and any(i.islower() for i in string) and any(i.isdigit() for i in string) and len(string) >= 8)
# or
    pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")
    return bool(pattern.match(string))

    
    
print(password("Abcd1234"), True)
print(password("Abcd123"), False)
print(password("abcd1234"), False)
print(password("AbcdefGhijKlmnopQRsTuvwxyZ1234567890"), True)
print(password("ABCD1234"), False)
print(password("Ab1!@#$%^&*()-_+={}[]|\:;?/>.<,"), True)
print(password("!@#$%^&*()-_+={}[]|\:;?/>.<,"), False)
print(password(""), False)
print(password(" aA1----"), True)
print(password("4aA1----"), True)
