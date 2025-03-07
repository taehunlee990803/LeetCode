class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        temp = [i for i in range(0, n+1)]

        for element in nums:
            temp.remove(element)
        # return temp - nums
        return temp[0]
        
