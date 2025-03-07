class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            current = nums[i]
            count = 0
            for j in range(len(nums)):
                if i != j and current > nums[j]:
                    count += 1
            ans.append(count)
        return ans 
