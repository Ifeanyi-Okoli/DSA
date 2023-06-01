""" 
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

get the 2

l = 0
r = len(numbers) - 1

while l < r:
    s = numbers[l] + numbers[r]
    if s == target: 
        return [l, r]
    elif s < target:

def twoSum(numbers, target):
    res = []
    
    for i, num in enumerate(numbers):
        j = i+1
        for j, num in enumerate(numbers):
            if target == numbers[i] + numbers[j]:
                return [i, j]
            j++
time complexity of O (n^2)


"""

class Solution(object):
    def twoSum(array, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
      
        l = 0
        r = len(array) - 1  # gives the last index of the array
        while l < r: # we have to keep moving the pointers from the left to right or from the right to left
            s= array[l] + array[r]
                #, 9
                #target = 9
            if s == target:                
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1 # decreases the value of r
                
    numbers = [2,7,11,15]
    target = 9
    print(twoSum(numbers, target))
    
    numbers = [2,3,4] 
    target = 6
    print(twoSum(numbers, target))