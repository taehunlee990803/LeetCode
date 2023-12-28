class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        # for first in range(0,len(height)):
        #     last = len(height) -first - 1
        while first <= last:
            x = height[first]
            y = height[last]

            if x > y:
                area = (last - first) *y
            else:
                area = (last - first) *x
                max_area = max(area, max_area)
                last -= 1
                max_area = max(area, max_area)
                first += 1
        first = 0
        last = len(height) - 1
        return max_area
[
