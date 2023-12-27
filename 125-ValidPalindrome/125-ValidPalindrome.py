class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert_letter = ""
        # for element in s:
        #     if element.isalpha() or element.isnumeric():
        #         convert_letter += element.lower()
        # reverse_letter = convert_letter[::-1]

        # print(reverse_letter)
        # print(convert_letter)
        # if len(s) == 1:
        #     return True
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]
        # return reverse_letter == convert_letter
"
