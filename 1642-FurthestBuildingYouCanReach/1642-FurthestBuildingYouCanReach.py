        #         elif bricks > 0 and ladders == 0:
        #                 bricks -= dif
        #                 ladders -= 1
        #             else:
        #         dif = next - current
        #         if bricks > 0 and ladders > 0:
        #             if bricks <= dif:
        #         continue
        #     elif current < next:
        #     if current >= next:
        #     next = heights[i+1]
        #     current = heights[i]
        # for i in range(len(heights)-1):

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
class Solution:
        heap = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(heap, diff)
            if len(heap) > ladders:  # Use bricks for the smallest diff first
                bricks -= heapq.heappop(heap)
            if bricks < 0:  # Not enough bricks to move to the next building
                return i
        return len(heights) - 1
[
