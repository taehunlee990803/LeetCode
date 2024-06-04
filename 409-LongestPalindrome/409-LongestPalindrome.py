class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ans = len(t)
        r = 0
        for element in s:
            if element == t[r]:
                ans -= 1
            
        # print(ans, maxNum)
                if ans == 0:
                    return 0
        temp = 0
                r += 1
        return ans
"
