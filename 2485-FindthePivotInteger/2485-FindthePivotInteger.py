class Solution:
    def pivotInteger(self, n: int) -> int:
        ans = -1 
        for i in range(0,n+1):
            left = 0
            right = 0
            for j in range(0,i+1):
                left += j
            for j in range(i,n+1):

                right += j
            if left == right:
                return i
        return -1 
        
8
