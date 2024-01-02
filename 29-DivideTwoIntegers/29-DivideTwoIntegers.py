        # if dividend == 0 or divisor == 0:
        #     return 0
        
       
        # if divisor == dividend:
        #     return 1
        
        # count = 0
        # absDividend = abs(dividend)
        # absDivisor = abs(divisor)
        # if absDividend == absDivisor:
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # count = 0
        # if dividend == 1:
        sign = -1 if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor >= 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = len(range(0, dividend-divisor+1, divisor))
        if sign == -1:
            result = -result
        minus_limit = -(2**31)
        plus_limit = (2**31 - 1)
        result = min(max(result, minus_limit), plus_limit)
        return result
-
