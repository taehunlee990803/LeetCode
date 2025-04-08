class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        col = []
        # 00, 10, 20
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[0])):
                temp.append(grid[j][i])

            col.append(temp)
        for element in col:

        count = 0
            for row in grid:
                    count += 1
        return count 


                if element == row:
            #     # print(element, row)
            #     count += 1
            # if element in grid:
        
