    def customSortString(self, order: str, s: str) -> str:
        junk = ""
        temp = ""

        for element in s:
            if element not in order:
                junk += element
            else:
                temp += element

        s = Counter(temp)
        for element in order:
            if element in s:
        ans = ""
                ans += element * s[element]
        ans += junk

class Solution:
"
