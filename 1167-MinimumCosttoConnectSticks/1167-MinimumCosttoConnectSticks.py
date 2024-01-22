class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 1:
            return 0

        cost = 0
        while len(sticks) >= 2:
            sticks.sort()

            cost += temp
            sticks.remove(sticks[0])
            sticks.remove(sticks[0])
        return cost 

            
            temp = (sticks[0] + sticks[1])
            sticks.append(temp)

[
