class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for element in counter:
        length = len(nums) // 2
            if counter[element] > length:
                return element 
[
