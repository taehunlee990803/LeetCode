                temp.append(tempMax)
        
                    for l in range(j-1, j+2):
                        tempMax = max(tempMax, grid[k][l])
            ans.append(temp)
        return ans 
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = []
        one = 0
        for i in range(1, n-1):
            temp = []
            for j in range(1, n-1):
                tempMax = 0
                for k in range(i-1, i+2):
class Solution:
[
