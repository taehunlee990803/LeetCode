class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e','i','o','u']
        temp = []
        for element in s:
            if element.lower() in vowels:
                temp.append(element)
        for i in range(len(s)):
            if s[i].lower() in vowels:
                ans += temp[-1-n]
        n = 0
                n += 1
        return ans
        print(temp)
        ans = ""
            else:
                ans += s[i]

