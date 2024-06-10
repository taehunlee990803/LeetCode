class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        for i in range(len(heights)):
        temp = sorted(heights)
            if heights[i] != temp[i]:
                count += 1
        return count 

[
