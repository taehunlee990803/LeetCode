class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        space_check = True
        word = []
        result = []
        for i in range(len(s)-1,-1,-1):
            if s[i] == " ":
                if space_check:
                    word.reverse()
                    result+=word
                    result+=" "
                    space_check = False
                    word = []
            else:
                word.append(s[i])
                space_check = True

        if len(word) > 0:
            word.reverse()
            result+=word
        
        return ''.join(result).strip()

        
