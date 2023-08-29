""" 
Your task is simply to count the total number of lowercase letters in a string.

Examples
"abc" ===> 3

"abcABC123" ===> 3

"abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 3

"" ===> 0;

"ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 0

"abcdefghijklmnopqrstuvwxyz" ===> 26
"""

def lowercase_count(strng):
    # Your code here
    return sum(1 for c in strng if c.islower())
    
    
    
print(lowercase_count("abc"), 3)
print(lowercase_count("abcABC123"), 3)
print(lowercase_count("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), 3)
print(lowercase_count(""), 0)
print(lowercase_count("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), 0)
print(lowercase_count("abcdefghijklmnopqrstuvwxyz"), 26)