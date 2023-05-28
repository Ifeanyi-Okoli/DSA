"""Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.
"""

class Solution(object):
    def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = nums[0]
        max_sum = 0
        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(max_sum, cur_sum)
        return max_sum
    
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))
    nums = [5,4,-1,7,8]
    print(maxSubArray(nums))