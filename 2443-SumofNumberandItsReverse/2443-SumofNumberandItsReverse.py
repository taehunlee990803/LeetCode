    
        # if num == 0 or num == 2:
    def sumOfNumberAndReverse(self, num: int) -> bool:
class Solution:
        #     return True
        # for i in range(1,num):
        #     temp = str(num - i)
        #     temp_rev = temp[::-1]
        #     if int(temp_rev) + i == num:
        #         print(i, temp)
        #         return True
        # return False

        for i in range(0, num+1):
            temp = str(i)
            temp = temp[::-1]
            temp = int(temp)
            if i + temp == num:
                return True
        return False
        
2
