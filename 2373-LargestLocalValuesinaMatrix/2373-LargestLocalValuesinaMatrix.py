    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = []
        one = 0
                temp.append(tempMax)
        for i in range(n):
            for j in range(3):
                currentMax = 0
                temp = []
                for x in range(3):
        for i in range(1, n-1):
            temp = []
            for j in range(1, n-1):
                tempMax = 0
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        tempMax = max(tempMax, grid[k][l])
            ans.append(temp)
        return ans 
[
