









        return False 


                n -= 1
        if n <= 0:
            return True
        f = [0] + flowerbed + [0]
        for i in range(1, len(f)-1):
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
                f[i] = 1
