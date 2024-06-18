class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(math.sqrt(c))
        sumValue = c
        while l <= r :
        #     templ = math.sqrt(l)
            current = l*l + r*r
            if current == c:
                return True
            elif current > c:

                r -= 1
           
        return False
            else:
                l += 1
5
