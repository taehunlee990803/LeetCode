






            count = max(tempCount, count)
            if s[i+k-1] in vowels:
                tempCount += 1
                tempCount -= 1
            # tempCount = prev
            if s[i-1] in vowels:
                count += 1
        for i in range(1,len(s)-k+1):
        for element in temp:
            if element in vowels:
        temp = s[:k]
        count = 0
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e','i','o','u']
        return count 
        tempCount = count


