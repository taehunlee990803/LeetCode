        ans = ""








    def mergeAlternately(self, word1: str, word2: str) -> str:
class Solution:
        while l < len(word1) and r < len(word2):
        l = r = 0
            ans += word1[l]
            ans += word2[r]
            l += 1
            r += 1
        if len(word1) < len(word2):
            ans += word2[r:]
        else:
            ans += word1[l:]
        return ans 

