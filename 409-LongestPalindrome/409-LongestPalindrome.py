    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        dic = {}
        for alpha in s:
            if alpha in dic:
                dic[alpha] += 1
            else:
                dic[alpha] = 1
        count = 0

        for element in dic:
            if dic[element] %2 == 0:
                count += dic[element]
            else:
        temp = 0
                temp = 1
        if temp == 1:
            return count + 1
        else:
        if len(dic) == 1:
            return len(s)
                current = dic[element]
                while current > 2:
                    count += 2
                    current -= 2
"
