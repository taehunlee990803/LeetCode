class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1,n+1):
        count = 0
            if n % i == 0:
                count += 1
                if count == k:
                    return i
        return -1 
        
1
