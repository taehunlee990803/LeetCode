class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        container = {}

        for num in nums:
            if num not in container:
                container[num] = 1
            else:
                return True
        return False

