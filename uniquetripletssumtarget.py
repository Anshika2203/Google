# Give a array of numbers. Find all the unique triplets in the array which gives the sum of given target.
# Example: Given array nums = [1, 3, 5, 7, 8, 8, 11, 13] target = 18
# answer would be [1,7,8] only one in this case

from typing import List

def findTriplets(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    result = []
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, n - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == target:
               
                result.append([nums[i], nums[left], nums[right]])
                
                
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            
            elif total < target:
                left += 1 
            else:
                right -= 1  
    
    return result

# Example usage
nums = [1, 3, 5, 7, 8, 8, 11, 13]
target = 18
print(findTriplets(nums, target))
