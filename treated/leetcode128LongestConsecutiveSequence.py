""" 
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

class Solution(object):
    def longestConsecutive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort the array
        # then find the longest consecutive sequence
        # O(nlogn) + O(n)
        # O(nlogn)
        # O(n)
        if not nums:
            return 0
        nums.sort()
        longest = 1
        current = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                current += 1
            else:
                current = 1
            longest = max(longest, current)
        return longest
    
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(longestConsecutive(nums))
    
    nums = [100,4,200,1,3,2]
    print(longestConsecutive(nums))