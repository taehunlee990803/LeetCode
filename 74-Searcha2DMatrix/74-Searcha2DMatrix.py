class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        prev = 0

        for element in matrix:
            if target in element:
                return True
            prev = element[-1]

            
            if target < prev:
                return False
        return False
[
