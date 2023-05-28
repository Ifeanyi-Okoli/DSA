// """Given an integer array nums, find the 
// subarray
//  with the largest sum, and return its sum.
// """

// class Solution(object):
//     def maxSubArray(nums):
//         """
//         :type nums: List[int]
//         :rtype: int
//         """
//         cur_sum = nums[0]
//         max_sum = 0
//         for i in range(1, len(nums)):
//             cur_sum = max(nums[i], cur_sum + nums[i])
//             max_sum = max(max_sum, cur_sum)
        // return max_sum
    // 

    function maxSubArray(nums){
        let cur_sum = nums[0]  // Initialize the current sum with the first element of the array
        let max_sum = 0  // Initialize the maximum sum to 0
        for(let i = 1; i < nums.length; i++){  // Iterate over the array starting from the second element
            cur_sum = Math.max(nums[i], cur_sum + nums[i])  // Update the current sum by taking the maximum between the current element and the sum of the current element and the previous sum
            max_sum = Math.max(max_sum, cur_sum)  // Update the maximum sum by taking the maximum between the current maximum sum and the current sum
        }
        return max_sum  // Return the maximum sum
    }
    


let nums = [-2,1,-3,4,-1,2,1,-5,4]
console.log(maxSubArray(nums))
nums = [5,4,-1,7,8]
console.log(maxSubArray(nums))