class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # heapq.heapifty(stones)

        while len(stones) >= 2:
            stones.sort()
            big = stones[-1]
        if len(stones) == 1:
            small = stones[-2]
            if big == small:
                stones.remove(big)
                stones.remove(small)
            else:
                stones.remove(small)
                stones.append(big-small)
            return stones[0]
        else:
            return 0
            # print(big, small)
            # stones.remove(big)
                stones.remove(big)
        # return stones[0]
[
