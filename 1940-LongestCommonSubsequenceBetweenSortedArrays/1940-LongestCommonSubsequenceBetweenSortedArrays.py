class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        temp = arrays[0]
        container = []
        for element in temp:
            check = True
            for array in arrays:
                if element not in array:
                    check = False
                    break
            if check:
                container.append(element)
        return container 
        
[
