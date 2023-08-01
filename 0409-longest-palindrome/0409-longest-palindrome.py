class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter_dict = dict(Counter(s))
        
        print(counter_dict)
        count = 0
        sum = 0
        for element in counter_dict:
            if counter_dict[element] %2 == 0:
                sum += counter_dict[element]
            else:
                sum += counter_dict[element] - 1 #1개면 불가능, 3개면 2개만 사용 
                count = 1
                
        return sum + count
