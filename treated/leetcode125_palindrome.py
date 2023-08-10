""" 
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 
 ABA
 ABA
 ABBA
 Nigeria
 AIREGIN 
 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
racaecar
Output: false
Explanation: "raceacar" is not a palindrome.
"""

class Solution(object):
    def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        print(s)
        str = ""    #Extra memory needed
        for c in s:
            if c.isalnum():
                str += c.lower()
        print(str)
        return str == str[::-1] #Extra memory used
       
    
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))
    # s = "race a car"
    # print(isPalindrome(s))
    
    # s = "ABBA"
    # print(isPalindrome(s))
    
    # s = "Nigeria"
    # print(isPalindrome(s))