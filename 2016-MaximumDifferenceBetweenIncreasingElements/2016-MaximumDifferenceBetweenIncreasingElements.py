class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_diff = nums[0]
        max_diff = 0

        for element in nums[1:]:
            max_diff = max(max_diff, element - min_diff)
            min_diff = min(element, min_diff)
        if max_diff == 0:
            return -1
        return max_diff
[
