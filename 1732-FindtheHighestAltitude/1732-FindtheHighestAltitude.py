class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        for i in gain:
            val = res[-1] + i
            res.append(val)
        return max(res)

