        #                     else:
        #                         temp = True
        #                         break
        #                     k+=1
        #             if temp:
        #                 break       
        #         ans += countZero*countOne

        #                         countZero += 1
        #                 while k < len(s):
        #                     if s[k] == '0':
        #             if s[k] == '0':
        #             if temp is False:
        #                 break
        #         for k in range(j, len(s)):
        #                     else:
        #                         temp = False
        #                         break
        #                     j+=1
        #         for j in range(i+1, len(s)):
        #             if s[j] == '1':
        #                 while j < len(s):
        #                     if s[j] == '1':
        #                         countOne += 1
        # ans = 0
        # for i in range(len(s)-2):
        #     if s[i] == '0':
        #         countOne = 0
        #         countZero = 0
        #         temp = True
class Solution:
    def numberOfWays(self, s: str) -> int:
        total_zeros = s.count('0')
        total_ones = s.count('1')
        count_0, count_1 = 0,0

        ans = 0
        for char in s:
            if char == '0':
            else:

                ans += count_1*(total_ones - count_1)
                count_0 += 1
                ans += count_0*(total_zeros - count_0)
                count_1 += 1
        return ans 
"
