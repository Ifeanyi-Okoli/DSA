""" 
Write a function which removes from string all non-digit characters and parse the remaining to number. E.g: "hell5o wor6ld" -> 56

Function:

getNumberFromString(s)
"""

def get_number_from_string(string):
    res=''
    for i in range(0, len(string)):
        if string[i].isdigit(): res += string[i]
    return int(res)

tests = (
    ("1", 1),
    ("123", 123),
    ("this is number: 7", 7),
    ("$100 000 000", 100000000),
    ("hell5o wor6ld", 56),
    ("one1 two2 three3 four4 five5", 12345),
)

for t in tests:
    inp, exp = t
    print(get_number_from_string(inp), exp)
    
# or

def get_number_from_string(string):
    return int(''.join(x for x in string if x.isdigit()))