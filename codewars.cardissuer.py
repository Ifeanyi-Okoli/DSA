""" 
Given a credit card number we can determine who the issuer/vendor is with a few basic knowns.

Complete the function get_issuer() that will use the values shown below to determine the card issuer for a given card number. If the number cannot be matched then the function should return the string Unknown.
"""


def get_issuer(number):
  # code your solution here
    number = str(number)
    for i in range(len(number)):
        if len(number) == 15 and number[0] == "3" and number[1] in ["4","7"]:
            return "AMEX"
        elif len(number) == 16 and number[0] == "5" and number[1] in ["1","2","3","4","5"]:
            return "Mastercard"
        elif len(number) in [13,16] and number[0] == "4":
            return "VISA"
        elif len(number) == 16 and number[0] == "6" and number[1] == "0" and number[2] == "1" and number[3] == "1":
            return "Discover"
        else:
            return "Unknown"

print(get_issuer(4111111111111111), 'VISA')
print(get_issuer(378282246310005), 'AMEX')
print(get_issuer(9111111111111111), 'Unknown')