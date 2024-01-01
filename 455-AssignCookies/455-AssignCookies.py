class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # max_num = 0
        # childrem = Counter(g)
        # cookies = Counter(s)

        # for element in g:
        #     for cookie in s:
        #         if int(cookie) >= element and cookie in cookies:
        #             if cookies[cookie] >=1:
        #                 cookies[cookie] -= 1
        #                 max_num += 1
        #                 break
        g.sort()
        s.sort()
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i+=1
            j+=1
        return i
        # return max_num
[
