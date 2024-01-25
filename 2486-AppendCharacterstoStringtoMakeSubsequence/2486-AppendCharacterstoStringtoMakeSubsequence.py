class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ans = 0

        temp = 0

        for element in s:
            if element == t[temp] and temp < len(t):
                temp+=1

        if temp < len(t):
        else:
            return len(t) - temp
            return 0
                if temp == len(t):
                    return 0
        # return len(t) - temp
"
