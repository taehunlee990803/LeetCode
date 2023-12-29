        # col_data ={i:set() for i in range(n)}

        # for row_i, row in enumerate(matrix):
        #     for col_i, num in enumerate(row):
        #         if num <

        for row in matrix:
            # dic = Counter(row)
            ans = []
            for element in row:
                if element in ans:
                    return False
                ans.append(element)

        for i in range(0,n):
            ans = []
            for j in range(0,n):
                if matrix[j][i] in ans:
                    return False
            if len(ans) != n:
                return False
                ans.append(matrix[j][i])
            if len(ans) != n:
                return False
        return True
        # row_data ={i:set() for i in range(n)}
        n = len(matrix)
    def checkValid(self, matrix: List[List[int]]) -> bool:
class Solution:
[
