class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1 
        l = 0
        r = len(nums)-1

        while l<=r :
            m = (l+r)//2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                if nums[l] >= target:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] > target:
                if nums[l] <= target:
                    r = m - 1
