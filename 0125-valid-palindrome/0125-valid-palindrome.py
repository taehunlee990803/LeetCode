class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_arr = []
        for i in range(len(s)):
            if s[i].isalnum():
                new_arr.append(s[i].lower())
        
        length = len(new_arr)
        for begin in range(length // 2):
            end = length - begin - 1
            if new_arr[begin] != new_arr[end]:
                return False
        return True