class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # possible = 0
        #     if i == 0:
        #     elif i == len(flowerbed)-1:
        #             possible += 1
        #             flowerbed[i] = 1
        #             possible += 1
        #             flowerbed[i] = 1
        #     else:
        #         if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
        #             possible += 1
        #             flowerbed[i] = 1
        #         if flowerbed[i] == 0 and flowerbed[i-1] == 0:
        #         if flowerbed[i] == 0 and flowerbed[i+1] == 0:
        # if len(flowerbed) == 1:
        #     if flowerbed[0] == 1:
        #         if n == 0:
        #     else:
        # for i in range(len(flowerbed)):
        #         if n <= 1:
        #             return True
        #         else:
        #             return False
        #             return True
        #         else:
        #             return False
        f = [0] + flowerbed + [0]
        for i in range(1, len(f)-1):
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
                n -=1 
                f[i] = 1

        return n <= 0
