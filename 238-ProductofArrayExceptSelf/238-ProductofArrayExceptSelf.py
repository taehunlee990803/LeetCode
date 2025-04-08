class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans = []*len(nums)
        

        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in range(len(nums)):

        prev = 1

            left[i] = prev
            prev *= nums[i]
        
        return ans 
        
        for i in range(len(nums)):
            right[i] = prev
            prev *= nums[len(nums)-1-i]
        prev = 1
        ans = [1] * len(nums)

        for i in range(len(nums)):
            ans[i] = (left[i] * right[len(nums)-1-i])
