""" 
FirstFactorial(num) take the num parameter being passed and return the factorial of it. For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between 1 and 18 and the input will always be an integer.
Examples
Input: 4
Output: 24
"""
from math import factorial
def FirstFactorial(num):

  # # code goes here
  # if num <= 1:
  #   return 1

  # return num*FirstFactorial(num-1)
  # # or
  # return num * FirstFactorial(num - 1) if num > 1 else 1
  return factorial(num)

# keep this function call here 
print(FirstFactorial(4))