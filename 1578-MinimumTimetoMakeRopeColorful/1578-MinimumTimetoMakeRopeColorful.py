class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        minimum = 0
        # neededTime./sort()
        l =0
        r = len(neededTime)-1
        count = 0
        container = []
        for i in range(0,len(neededTime)-1):
            if colors[i] == colors[i+1]:
                container.append(i)
"abaac"
[1,2,3,4,5]
"abc"
[1,2,3]
"aabaa"
