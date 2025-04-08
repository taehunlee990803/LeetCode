class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = [0] * len(nums)
        right = [0] * len(nums)

        prefix = 0
        for i in range(len(nums)):
            left[i] = prefix
            prefix += nums[i]
        postfix = 0
        for i in range(len(nums)-1,-1,-1):
            right[len(nums)-1-i] = postfix
            postfix += nums[i]
        
        for i in range(len(nums)):
            if left[i] == right[len(nums)-1-i]:
                return i
        return -1 

