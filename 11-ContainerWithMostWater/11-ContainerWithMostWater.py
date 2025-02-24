
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            area = w*h
            max_area = max(max_area, area)
        return max_area

class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0
        r = len(height)-1
        max_area = 0

            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1            
