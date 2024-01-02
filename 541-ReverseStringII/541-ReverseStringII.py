class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            return s[::-1]
        ans = ""
        while i < len(s):
            # left = len(s)-i+1
            # if left < k:
            #     ans += s[i:len(s):-1]
            # elif left >= k and left < 2*k:
            #     ans +=  s[i:i+k:-1]
            #     ans += s[i+k:i+2*k]
        return ans 
                ans += s[i+k:i+2*k]
            if i + 2*k < len(s):
                temp =  s[i:i+k]
                i += 4
            elif i +2*k >= len(s) and i + k < len(s):

                temp =  s[i:i+k]
                ans += temp[::-1]
        i = 0
                ans += temp[::-1]
                ans += s[i+k:len(s)]
                return ans
"
