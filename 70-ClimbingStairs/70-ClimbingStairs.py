        # dp = [0] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1

        # for i in range(2, n + 1):
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        # 3
        # 1 + 1 + 1 = 2 + 1 = 1 + 2
        return dp[-1]
        # dp[3] = dp[1] + dp[2] = 2 + 1 = 3
        # dp[2] = dp[0] + dp[1] = 1 + 1 = 2

        dp[1] = 1
        dp[0] = 1
        dp = [0] * (n+1)

    def climbStairs(self, n: int) -> int:
class Solution:
