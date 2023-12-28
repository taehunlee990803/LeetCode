class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        max_length = 1
        # for element in s:
        #         if element in dic:
        #             dic = {}
        #         else:
        #             dic[element] = 1
        #             count = 1
        #             dic[element] = 1
        count = 0
        if len(s)==1:
            return 1
        #     for 
        for i in range(0,len(s)):
            for j in range(i+1, len(s)):
            dic = {}
            dic[s[i]] = 1
                if s[j] not in dic:
                    dic[s[j]] = 1
            count = 1
                    count += 1
                else:
                    break
                    max_length = max(count, max_length)
        return max_length
        if len(s) == 0:
            return 0
"
