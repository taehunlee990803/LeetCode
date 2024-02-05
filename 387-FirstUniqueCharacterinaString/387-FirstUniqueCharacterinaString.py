class Solution:
    def firstUniqChar(self, s: str) -> int:
        container = []
        for i in range(len(s)):
        temp = Counter(s)

            if temp[s[i]] == 1:
                return i
        return -1
        
"
