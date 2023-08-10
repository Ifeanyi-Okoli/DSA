""" 
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 
  01 >> 1
  10 >>> 2
 000  >>> after th AND and shift operation
11 >>> after Xclusive OR operation
00
 <<1


000
110
000


Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5

"""
# 2 = 10

# and
# ^ Exclusive OR
# & Exclusive AND
#<< 1
#Temp vriable

class Solution(object):
    def getSum(a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 01
        # b= 10
        while (b != 0):
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return a
            
        
        
    a = 1
    b = 2
    print(getSum(a, b))
    
    a = 9
    b = 2
    print(getSum(a, b))