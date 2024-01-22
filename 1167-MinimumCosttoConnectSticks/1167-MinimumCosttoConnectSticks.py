class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        # if len(sticks) == 1:
        #     return 0

        # cost = 0
        # while len(sticks) >= 2:
        #     sticks.sort()
        #     temp = (sticks[0] + sticks[1])
        #     cost += temp
        #     sticks.remove(sticks[0])
        #     sticks.remove(sticks[0])
        #     sticks.append(temp)
            

        heapq.heapify(sticks)
        sum = 0 
        while len(sticks) >= 2:
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)
            sum += first + second
            heapq.heappush(sticks, first+second)
        return sum
[
