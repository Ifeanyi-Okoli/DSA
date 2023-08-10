""" 
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""

def countSubstrings(s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
                
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count
    
    
#             res += helper(s, i, i) + helper(s, i, i + 1)
#         return res
# def helper(s, l, r):
#     count = 0
#     while l >= 0 and r < len(s) and s[l] == s[r]:
#         count += 1
#         l -= 1
#         r += 1
#     return count
    
s = "abc"
print(countSubstrings(s))

s = "aaa"
print(countSubstrings(s))

s = "hannah"
print(countSubstrings(s))