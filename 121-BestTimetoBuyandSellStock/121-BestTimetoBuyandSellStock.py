class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        # for i in range(len(prices)):
        #     current = prices[i]
        #     for j in range(i+1, len(prices)):
        #         if current < prices[j]:
        #             maxProfit = max(maxProfit, prices[j] - current)
        # return maxProfit
        l,r = 0,1
        while r != len(prices):
            if prices[l] < prices[r]:
                maxProfit = max(prices[r]-prices[l], maxProfit)
            else:
                l = r
            r+=1
        return maxProfit
