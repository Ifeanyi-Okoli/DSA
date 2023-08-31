""" 
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
"""


def valid_parentheses(paren_str):
    # open_paren = 0
    # if paren_str.startswith(")") or paren_str.endswith("("):
    #     return False
    # for i in paren_str:
    #     if i == "(":
    #         open_paren += 1
    #     elif i == ")":
    #         open_paren -= 1
    #         if open_paren < 0:
    #             return False
    # return open_paren == 0
    # or
    while "()" in paren_str:
        paren_str = paren_str.replace("()", "")
    return not paren_str


print(valid_parentheses("()"))
print(valid_parentheses(")(()))"))
print(valid_parentheses("(())((()())())"))
print(valid_parentheses("("))
