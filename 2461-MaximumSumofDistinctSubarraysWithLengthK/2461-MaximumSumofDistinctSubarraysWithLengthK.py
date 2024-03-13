        #     if nums[i] not in container:
        # check = True
        # index = 0
        # for i in range(k):
        #         return nums[0]

        # if len(nums) == 2:
        #     if k == 1:
        #         return max(nums)
        #     elif k == 2:
        #         return sum(nums)

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
         # maxSum = 0
        # two = []
        # container = []
        # if len(nums) == 1:
        #     if k > 1:
        #         return 0
        #     else:
        seen = Counter(nums[:k])
        summ = sum(nums[:k])
    
        if len(seen) == k:
            res = summ
        res = 0

        for i in range(k, len(nums)):
            summ += nums[i]
            summ -= nums[i-k]

            seen[nums[i]] += 1
            seen[nums[i-k]] -= 1
            if seen[nums[i-k]] == 0:
                del seen[nums[i-k]]
            if len(seen) == k:
                res= max(res, summ)
        return res 
[
