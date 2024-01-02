class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        half = num//2
        temp = 0
        for i in range(1,half+1):
            if num%i == 0:
                temp+=i
                if temp > num:
                    return False
        if num%2 != 0:
            return False
        return temp == num
2
