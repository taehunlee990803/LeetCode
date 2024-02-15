class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for element in words:
            temp = len(element)-1
            check = True
            for i in range(len(element)):
                if element[i] != element[temp]:
                    check = False

                    break
                temp -= 1
            if check:
                return element
        return ""
[
