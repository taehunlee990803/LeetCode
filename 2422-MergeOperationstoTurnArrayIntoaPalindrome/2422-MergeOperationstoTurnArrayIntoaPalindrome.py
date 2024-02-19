class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        l,r = 0, len(nums)-1

        while l <= r:
            if nums[l] == nums[r]:
                l+=1
                r-=1
            else:
                left = nums[l] + nums[l+1]
                right = nums[r] + nums[r-1]
                if left < right:
                    nums[l+1] += nums[l]
                    l+=1
                else:
                    nums[r-1] += nums[r]
                    r-=1
                count +=1 

        return count 
            
[
