class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(n):
            temp = pow(3,i)
            if temp == n:
                return True
            if temp > n:
                return False
        return False
2
