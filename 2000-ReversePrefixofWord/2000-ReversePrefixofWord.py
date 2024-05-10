class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        temp = ""
        for i in range(len(word)):
            if word[i] == ch:
                ans += temp[::-1]
        
        ans = ""
                temp += ch
                ans += word[i+1:]

                return ans
            else:
                temp += word[i]
        return ans 
        
"
