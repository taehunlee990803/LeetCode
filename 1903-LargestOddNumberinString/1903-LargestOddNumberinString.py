class Solution:
    def largestOddNumber(self, num: str) -> str:
        maxValue = 0

        for i in range(len(num)-1,-1,-1):
        else:
            for i in range(len(num)):

                if int(num[i]) %2 != 0:
                    maxValue = max(maxValue, int(num[i]))
        if maxValue == 0:
            return ""
        else:
            return str(maxValue)
            if int(num[i]) % 2 != 0:
                return num[:i+1]
        
"
