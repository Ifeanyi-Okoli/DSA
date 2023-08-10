""" 
Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples (a, b) --> output (explanation)
"""

# def get_sum(a,b):
#     #good luck!
#     if a==b:
#         return a
#     return sum(range(a+1,b))+a+b

# ///////////////////////////////////

def get_sum(a,b):
    #good luck!
    sum =0
    min = a if a<b else b
    for i in range(min,a+b-min+1):
        sum += i
    return sum
    
print(get_sum(0,1),1)
print(get_sum(0,-1),-1)
    