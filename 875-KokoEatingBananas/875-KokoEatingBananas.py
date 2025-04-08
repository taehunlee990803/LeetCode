class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k can be 1 to max element of piles 

        maxElement = max(piles)

        l = 1
        r = maxElement
        res = r
        while l <= r:
            k = (l+r) // 2
            for p in piles:
            hours = 0
                hours += math.ceil(p/k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res

