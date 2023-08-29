""" 
Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a digit (0-9), false otherwise.
"""

def is_digit(n):
    #your code here
    if len(n) != 1:
        return False
    return bool(n.isdigit())

print(is_digit(""), False)
print(is_digit("7"), True)
print(is_digit(" "), False)
print(is_digit("a"), False)
print(is_digit("a5"), False)