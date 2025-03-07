class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        word1_len = len(word1)
        word2_len = len(word2)
        if word1_len >= word2_len:
            for i in range(word2_len):
                ans += word1[i]
        else:
                ans += word2[i]
            ans += word1[i+1:]
            for i in range(word1_len):
                ans += word1[i]
                ans += word2[i]
            ans += word2[i+1:]
            
        return ans 
