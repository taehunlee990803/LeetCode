class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # ans = 0
        # points.sort()

        # total = len(points)
        # temp = 0
        # first = points[temp][1]

        #     # print(points[i][0], points[i][1], first,ans)
        #     # if points[i][0] > first or points[i][1] < first:
        #     #     ans += 1
        #     #     if i != len(points)-1:
        #     if points[i][0] <= first and points[i][1] >= first:
        #         ans += 1
        #     else:
        #         first = points[i][1]
        # for i in range(1, len(points)):
        if not points:
            return 0

        points.sort(key=lambda x: x[1])  # Sort by end points

        ans = 1
        current_end = points[0][1]

        for balloon in points[1:]:
            start, end = balloon
            if start > current_end:
                ans += 1
                current_end = end

        return ans
        #     #         first = points[i+1][1]
        #     #     else:
[
