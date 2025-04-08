class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        l = 0
        r = len(nums)-1


        while l < r:
            if currentSum == k:
                l += 1
                r -= 1
                ans += 1
            else:
                if currentSum > k:

        nums.sort()

            currentSum = nums[l] + nums[r]
                    r -= 1
                else:
                    l += 1
        return ans 
