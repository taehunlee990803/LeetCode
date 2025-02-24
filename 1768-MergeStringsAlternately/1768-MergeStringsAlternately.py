class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        word2_length = len(word2)
        word1_length = len(word1)
        
        if word1_length >= word2_length:

        else:

            for i in range(0, word2_length):
                ans += word1[i]
                ans += word2[i]
            ans += word1[i+1:]
            for i in range(0, word1_length):
                ans += word1[i]
                ans += word2[i]
            ans += word2[i+1:]

        return ans

