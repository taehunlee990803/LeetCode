        # print(dp)
        # return ans 
        n = len(arr)

        # def dfs(i):
        #     if i == n:
        #         return 0
            
        #     curMax = curSum = 0

        #     for j in range(i, min(i+k,n)):
        #         curMax = max(curMax, arr[j])
        # for i in range(len(dp)):
        #     ans += dp[i]
        #             if j > 0 and j < len(arr):
        #                 temp = max(temp, arr[j])
        #     dp[i] = temp
        #     else:
        #         for j in range(i-1, i+k):
        #             if j > 0 and j < len(arr):
        #                 temp = max(temp, arr[j])
        #         for j in range(len(arr)-1, len(arr)-1-k, -1):
        #     elif i == len(arr)-1:
        #                 break

        dp = [0]*(n+1)
        for i in range(1, n+1):
            maximum = 0
            max_sum = 0 
            for j in range(1, k+1):
                if i - j >= 0:
                    maximum = max(maximum, arr[i-j])
                    max_sum = max(max_sum, dp[i-j] + maximum*j)
            dp[i] = max_sum
        return dp[n]
[
