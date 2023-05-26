"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
    """
    
# Solution:

def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        # Brute Force Solution
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        # Hash Table Solution
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        hash_table = {}
        for i in range(len(nums)):
            if target - nums[i] in hash_table:
                # If the complement of the current number exists in the hash table,
                # it means we have found a pair whose sum is equal to the target.
                # We return the indices of the complement and the current number.
                return [hash_table[target - nums[i]], i]
            # Store the current number in the hash table with its index as the value.
            hash_table[nums[i]] = i