        #     return nums
         # if len(nums) == 1:
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] ==0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key = len)
        dp = [ [i] for i in nums]
        nums.sort()
            return []
        if n == 0:
        n = len(nums)
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
[1,2,3]
