class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        count = 0
        ans = []
        if n == 0:
            return [0]
        for i in range(0,n+1):
            count = bin(i).count('1')
            ans.append(count)
        return ans