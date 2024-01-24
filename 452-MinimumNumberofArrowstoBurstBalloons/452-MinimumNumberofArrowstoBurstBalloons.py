class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])  # Sort by end points
        print(points)
        ans = 1
        current_end = points[0][1]

        for balloon in points[1:]:
            start, end = balloon
            if start > current_end:
                ans += 1
                current_end = end

        return ans
        # ans = 0
        # points.sort()
[[10,16],[2,8],[1,6],[7,12]]
