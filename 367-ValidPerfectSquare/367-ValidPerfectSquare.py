class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        num = math.sqrt(num)
        if num.is_integer():
            return True
        else:
            return False
       
1
