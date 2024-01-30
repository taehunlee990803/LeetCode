class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = math.inf
        s,e,sm = 0,0,0
        
        for e in range(len(nums)):
            sm += nums[e]

            while sm >= target:
                ans = min(ans, e-s+1)
                sm -= nums[s]
                s +=1 
        if ans == math.inf:
            return 0
        
        return ans
7
