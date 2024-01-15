class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        dic = {}

        for i in range(26):
            dic[keyboard[i]] = i
        
        # time = dic[word[0]]
        ans = dic[word[0]]
        # for i in range()
        for i in range(len(word)-1):
            first = dic[word[i]]
            second = dic[word[i+1]]
            ans += abs(first - second)
        return ans 
"
