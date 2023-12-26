class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        

        def helper(n):
            if n == 1 or n == 2:
                return True
            elif n < 2:
                return False
            else:
                return helper(n/2)
        return helper(n)
1
16
3
