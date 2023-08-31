""" 
Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. First argument is an array of numbers and the second is the divisor.

Example(Input1, Input2 --> Output)
[1, 2, 3, 4, 5, 6], 2 --> [2, 4, 6]
"""

def divisible_by(numbers, divisor):
    res =[]
    for i in numbers:
        if i%divisor == 0:
            res.append(i)
    return res
    #or
    return [i for i in numbers if i%divisor == 0]
    
    
    
print(divisible_by([1,2,3,4,5,6], 2), [2,4,6])
print(divisible_by([1,2,3,4,5,6], 3), [3,6])
print(divisible_by([0,1,2,3,4,5,6], 4), [0,4])
print(divisible_by([0], 4), [0])
print(divisible_by([1,3,5], 2), [])
print(divisible_by([0,1,2,3,4,5,6,7,8,9,10], 1), [0,1,2,3,4,5,6,7,8,9,10])