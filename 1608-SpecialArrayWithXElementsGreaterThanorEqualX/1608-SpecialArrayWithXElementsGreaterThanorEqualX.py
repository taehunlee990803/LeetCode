class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for element in range(0, len(nums)+1):
            temp = element
            count = 0
            for element in nums:
                if element >= temp:
                    count += 1
                return temp
        return -1 
            if count == temp:

[
