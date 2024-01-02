class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ans = ""
        if len(title) <= 2:
            for element in title:
                if ord(element) >= 65 and ord(element)<=90:
                    ans += chr(ord(element)+32)
                else:
                    ans+= chr(element)
            return ans
        
"
