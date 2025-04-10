
        n = len(matrix)
        for i in range(n):
        #     for j in range(n):
        #         heapq.heappush(minHeap, matrix[i][j])

            heapq.heappush(minHeap, (matrix[i][0], i, 0))
        



        return val
        #         if len(minHeap) > k:
        #             heapq.heappop(minHeap)
        # print(minHeap)
        for _ in range(k):
            val, r, c = heapq.heappop(minHeap)

            if c + 1 < n:

                heapq.heappush(minHeap, (matrix[r][c+1], r, c+1))
        minHeap = []
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
