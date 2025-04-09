





        #         dp[i][j] = 0

                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        # for i in range(n):
        #     for j in range(m):
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
        n = len(text1)
        m = len(text2)
        dp = [[0 for i in range(m+1)] for j in range(n+1)]

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return dp[0][0]

