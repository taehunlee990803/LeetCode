                    
                return ans
                i += 2*k
            elif i +2*k >= len(s):
                ans += s[i+k:i+2*k]
                ans += temp[::-1]
                if i+k < len(s):
                    temp =  s[i:i+k]
                else:
                    ans += temp[::-1]
                    ans += s[i+k:len(s)]
                    temp =  s[i:len(s)]
                    ans += temp[::-1]
                temp =  s[i:i+k]
            if i + 2*k < len(s):
        while i < len(s):
        i = 0
        ans = ""
            return s[::-1]
        if len(s) <= k:
            return s
        if k == 1:
class Solution:
    def reverseStr(self, s: str, k: int) -> str:

            # left = len(s)-i+1
"abcdefg"
