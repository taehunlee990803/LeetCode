class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # min_heap = []
        # for num in nums:
        #     heapq.heappush(min_heap, -num)
        #     # if len(min_heap) > k:
        #     #     heapq.heappop(min_heap)
        # print(min_heap)
        # return -min_heap[k-1]
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        for _ in range(k-1):
            heapq.heappop(max_heap)

        return -max_heap[0]





        
        # min_heap = []
