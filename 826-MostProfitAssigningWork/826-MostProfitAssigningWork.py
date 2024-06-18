class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) 
-> int:
        ans = 0
        count = len(profit)
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        maxfit = 0
        j = 0
        for work in worker:
            while j < len(jobs) and work >= jobs[j][0]:
                maxfit = max(maxfit, jobs[j][1])
                j += 1
            
            ans += maxfit
        return ans 
            
[
