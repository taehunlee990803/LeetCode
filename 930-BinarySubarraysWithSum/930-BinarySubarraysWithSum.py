    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # ans = 0
        # container = []
        # sum = 0
        # i = 0
        # for i in range(len(nums)):
        #     if sum < goal:
        #         sum += nums[i]
        #         container.append(nums[i])
        #         if sum == goal:
        #             ans += 1
        #     elif sum == goal:
        #         if nums[i] == 0:
        #             container.append(nums[i])
        #             ans += 1
        #         else:
class Solution:
        ans = 0
        prefixsum = 0
        res[0] = 1
        res = defaultdict(int)
        for i in nums:
            prefixsum += i
            ans += res[prefixsum - goal]
            res[prefixsum] += 1
        return ans 
[
