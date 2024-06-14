class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                temp = nums[i-1] - nums[i] +1
                count += temp
                nums[i] = nums[i-1]+1
        

                
        return count 
            
        
[1,2,2]
