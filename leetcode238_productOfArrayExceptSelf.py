"""  
238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

class Solution(object):
    def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
#         # Brute force: O(n^2)
#         # Time Limit Exceeded
#         res = []
#         for i in range(len(nums)):
#             product = 1
#             for j in range(len(nums)):
#                 if i != j:
#                     product *= nums[j]
#             res.append(product)
#         return res
        res = [1] * len(nums)
        left = 1
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]
        right = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return right            

    nums = [1,2,3,4]
    print(productExceptSelf(nums))                                      