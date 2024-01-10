class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        left = int(nums[-1]*nums[-2])
        right = int(nums[0]*nums[1])
        return left - right
        # return nums[-1]*[-2] - nums[0]*nums[1]
[5,6,2,7,4]
