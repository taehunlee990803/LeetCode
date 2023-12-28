class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # minimum = 0
        # # neededTime./sort()
        # l =0
        # r = len(neededTime)-1
        # count = 0
        # container = []
        # for i in range(0,len(neededTime)-1):
        #     if colors[i] == colors[i+1]:
        #         container.append(i)
        # print(container)
        # for element in container:
        #     if neededTime[element] <= neededTime[element+1]:
        #         temp = neededTime[element]
        #         neededTime[element] = neededTime[element+1]
                
        #     else:
        #         temp = neededTime[element+1]
        ans = 0
        prev = 0
        for i in range(1, len(colors)):
            if colors[prev] != colors[i]:
                prev = i
            else:
                ans += min(neededTime[prev],neededTime[i])
                if neededTime[prev] < neededTime[i]:
                    prev = i
        return ans
"
