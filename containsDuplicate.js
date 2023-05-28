function containsDuplicate(nums){
    let hashSet = new Set(); // Create an empty hash set to store unique elements
    for (let i = 0; i < nums.length; i++){ // Iterate through each element in the nums list
        if (hashSet.has(nums[i])){ // Check if the current element already exists in the hash set
            return true; // If it does, return True (duplicate found)
        } else {
            hashSet.add(nums[i]); // If it doesn't, add the element to the hash set
        }
    }
    return false; // If the loop completes without finding any duplicates, return False
}
   

nums = [1,1,1,3,3,4,3,2,4,2]
console.log(containsDuplicate(nums))
nums = [1,2,3,4]
console.log(containsDuplicate(nums))
nums = [1,2,3,1]
console.log(containsDuplicate(nums))