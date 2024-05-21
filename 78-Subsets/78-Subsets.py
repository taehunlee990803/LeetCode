class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        for i in range(1 << n):
            k = []
            for j in range(n):
                if ( i & (1 << j) != 0):
                    k.append(nums[j])
            ans.append(k)
        return ans 
[
