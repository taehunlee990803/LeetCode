        # max_num = nums[0]
        # sub_array = nums[0]

        # for num in nums[1:]:
        max_num = nums[0]
        sub_arr = nums[0]

        for num in nums[1:]:
            sub_arr = max(num, sub_arr + num)
    def maxSubArray(self, nums: List[int]) -> int:
class Solution:
            max_num = max(sub_arr, max_num)
        return max_num
