#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        while left < right:
        # t = n//2
    

        left = 1
        right = n
            mid = (left + right) // 2
            ans = guess(mid)
            if ans == 0:
                return mid
            elif ans == 1:
                left = mid + 1
            else:
                right = mid - 1
        return left
        
