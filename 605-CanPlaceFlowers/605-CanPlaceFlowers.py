class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        

        total_length = len(flowerbed)


        for i in range(total_length):
            if flowerbed[i] == 0:
                left_side = (i == 0) or (flowerbed[i-1] == 0)
                right_side = (i == total_length-1) or (flowerbed[i+1] == 0)

                if left_side and right_side:
                    n -= 1 
                    flowerbed[i] = 1

                    if n == 0:
                        return True
        return n <= 0

        
