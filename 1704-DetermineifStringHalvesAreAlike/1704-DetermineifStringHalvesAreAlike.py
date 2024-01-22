class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        lower = ['a','e','i','o','u']
        upper = ['A','E','I','O','U']
        countFirst = 0
        countSecond = 0
        dic_first = Counter(s[:length//2])
        dic_second = Counter(s[length//2:])
        for element in dic_first:
            if element in lower or element in upper:
                countFirst += dic_first[element]
        
        length = len(s)
        for element in dic_second:
            if element in lower or element in upper:
                countSecond += dic_second[element]
        
        return countFirst == countSecond

        
"
