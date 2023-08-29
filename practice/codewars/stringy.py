""" 
write me a function stringy that takes a size and returns a string of alternating 1s and 0s.

the string should start with a 1.

a string with size 6 should return :'101010'.

with size 4 should return : '1010'.

with size 12 should return : '101010101010'.

The size will always be positive and will only use whole numbers.
"""


def stringy(size):
    # Good Luck!
    # res = ""
    # for i in range(size):
    #     if i % 2 == 0:
    #         res += '1'
    #     else:
    #         res += '0'
    # return (res)
    return ('10'*size)


print(stringy(3), '101', 'stringy(3)')
print(stringy(5), '10101', 'stringy(5)')
print(stringy(12), '101010101010', 'stringy(12)')
print(stringy(26), '10101010101010101010101010', 'stringy(26)')
print(stringy(28), '1010101010101010101010101010', 'stringy(28)')

# or
# def stringy(size):
    # Good Luck!
    # res = ""
    # for i in range(size):
    #     if i % 2 == 0:
    #         res += '1'
    #     else:
    #         res += '0'
    # return (res)
    # return ('10'*size)
