class Solution:
    def makePalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        count = 2
        while l < r:
            if s[l] != s[r]:
                count -= 1
            l += 1
            r -= 1

        
        if count >= 0:
            return True
        print(count)
                if count < 0:
                    return False
        return False
"
