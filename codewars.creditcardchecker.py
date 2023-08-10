""" 
Description
Write a function that checks whether a credit card number is correct or not, using the Luhn algorithm.

The algorithm is as follows:

From the rightmost digit, which is the check digit, moving left, double the value of every second digit; if the product of this doubling operation is greater than 9 (e.g., 8 × 2 = 16), then sum the digits of the products (e.g., 16: 1 + 6 = 7, 18: 1 + 8 = 9) or alternatively subtract 9 from the product (e.g., 16: 16 - 9 = 7, 18: 18 - 9 = 9).
Take the sum of all the digits.
If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is valid according to the Luhn formula; else it is not valid.
The input is a string with the full credit card number, in groups of 4 digits separated by spaces, i.e. "1234 5678 9012 3456"
Don´t worry about wrong inputs, they will always be a string with 4 groups of 4 digits each separated by space.

Examples
valid_card?("5457 6238 9823 4311") # True

valid_card?("5457 6238 9323 4311") # False
"""

def valid_card(card):
    # Your code here
    card = card.replace(" ","")
    double_digits = []
    for i in range(len(card)-1,-1,-1):
        digit = int(card[i])
        if i % 2 != 0:
            double_digits.append(digit)
        else:
            double = digit * 2
            if double > 9:
                double_digits.append(double - 9)
            else:
                double_digits.append(double)
                
    return sum(double_digits) % 10 == 0
    
    
    

print(valid_card("5457 6238 9823 4311"), True)
print(valid_card("5457 6238 9823 4311"), True)
print(valid_card("8895 6238 9323 4311"), False)
print(valid_card("5457 6238 5568 4311"), False)
print(valid_card("5457 6238 9323 4311"), False)
print(valid_card("2222 2222 2222 2224"), True)
print(valid_card("5457 1125 9323 4311"), False)
print(valid_card("1252 6238 9323 4311"), False)
print(valid_card("9999 9999 9999 9995"), True)
print(valid_card("0000 0300 0000 0000"), False)
print(valid_card("4444 4444 4444 4448"), True)
print(valid_card("5457 6238 9323 1252"), False)
print(valid_card("5457 6238 1251 4311"), False)
print(valid_card("3333 3333 3333 3331"), True)
print(valid_card("6666 6666 6666 6664"), True)
print(valid_card("5457 6238 0254 4311"), False)
print(valid_card("0000 0000 0000 0000"), True)
print(valid_card("5457 1111 9323 4311"), False)
print(valid_card("5457 6238 9823 4311"), True)
print(valid_card("1145 6238 9323 4311"), False)
print(valid_card("8888 8888 8888 8888"), True)
print(valid_card("0025 2521 9323 4311"), False)
print(valid_card("5457 6238 9323 4311"), False)
print(valid_card("1111 1111 1111 1117"), True)
print(valid_card("1234 5678 9012 3452"), True)
print(valid_card("5458 4444 9323 4311"), False)
print(valid_card("5457 6238 3333 4311"), False)
print(valid_card("0123 4567 8901 2345"), False)
print(valid_card("5555 5555 5555 5557"), True)