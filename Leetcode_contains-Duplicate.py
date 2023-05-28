"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 Example 1:

Input: nums = [1,2,3,1]
Output: true"""

# class Solution(object):
def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    hash_set = set()  # Create an empty hash set to store unique elements
    for i in nums:  # Iterate through each element in the nums list
        if i in hash_set:  # Check if the current element already exists in the hash set
            return True  # If it does, return True (duplicate found)
        else:
            hash_set.add(i)  # If it doesn't, add the element to the hash set
    return False  # If the loop completes without finding any duplicates, return False


nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))
nums = [1,2,3,4]
print(containsDuplicate(nums))
nums = [1,2,3,1]
print(containsDuplicate(nums))