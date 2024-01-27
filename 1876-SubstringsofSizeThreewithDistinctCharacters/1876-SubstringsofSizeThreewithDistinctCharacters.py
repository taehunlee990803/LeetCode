class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            if len(s) - i >= 3:
                temp = []
                for j in range(i, i+3):
                    if s[j] in temp:

                        break
                    else:
                        temp.append(s[j])
                if check:
                        check = False
                check = True
                    ans += 1
        return ans 

"
