class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = Counter(nums)
        for element in dic:
            if dic[element] == 1:
                return element
        
[2,2,3,2]
