class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * length

        for i in range(1, length):
        length = len(nums)
            ans[i] = nums[i-1]*ans[i-1]

        for i in range(length-1, -1, -1):
            ans[i] = ans[i] * R
        R = 1
            R *= nums[i]
        return ans 
            
