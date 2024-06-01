class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = []
        dic = {}
        for element in nums:
            if element in dic:
                dic[element] += 1
            else:
                dic[element] = 1
        for element in dic:
            if dic[element] == 1:
                ans.append(element)
        return ans 
[
