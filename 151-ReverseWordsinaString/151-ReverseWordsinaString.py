class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        length = len(s)
        for i in range(length-1,-1,-1):
        temp = ""
            if s[i] != " ":
                ans += temp[::-1]


              
        
 

        check = False
                check = True
                if check:
                    ans += " "
                    check = False
        return ans 

        if temp != "":
                temp = ""
                # temp.append(s[i])
                temp += s[i]
            ans += temp[::-1]
            elif temp != "":
            
