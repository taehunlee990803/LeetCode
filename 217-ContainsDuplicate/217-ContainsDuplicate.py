class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {

        }
        for element in nums:
            if element in dict:
                return True
            else:
                dict[element] = 1
        return False
[1,2,3,1]
[1,2,3,4]
[1,1,1,3,3,4,3,2,4,2]
