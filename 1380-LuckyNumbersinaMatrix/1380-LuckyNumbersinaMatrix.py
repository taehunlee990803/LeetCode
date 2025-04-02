class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_container = [] # i th element would be the min element in i th row 
        max_container = []
        for element in matrix:
            temp = min(element)
            min_container.append(temp)

            tempContainer = []
            for i in range(len(matrix)): # 0,1,2,3
                current = matrix[i][j] 
                tempContainer.append(current)
            maxElement = max(tempContainer)
            max_container.append(maxElement)
        for element in min_container:
        return []
        
        for j in range(len(matrix[0])): # 0,1,2
        print(min_container, max_container)
            if element in max_container:
                return [element]
