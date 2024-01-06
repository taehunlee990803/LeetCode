            dp[i] = max(dp[i], dp[i - 1])
                dp[i] = max(dp[i], dp[prev_job_index] + jobs[i][2])

            if prev_job_index != -1:
            # Binary search to find the latest non-overlapping job
            prev_job_index = self.binary_search(jobs, i)

        # Initialize dp array with the profits
        for i in range(n):
            dp[i] = jobs[i][2]

        for i in range(1, n):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])  # Sort jobs by end time
        n = len(jobs)
        dp = [0] * n

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

[1,2,3,3]
