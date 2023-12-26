class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        i = 0

            if num[x] == '1':
                ans += pow(2,i)
            i += 1
        num = bin(n)[2:].zfill(32)
        for x in range(0,len(num)):
        return ans 
0
