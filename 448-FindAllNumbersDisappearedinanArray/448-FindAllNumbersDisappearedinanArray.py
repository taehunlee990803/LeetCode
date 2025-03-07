class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        set_nums = set(nums)
        ans = []
        temp = [i for i in range(1, n+1)]
        for element in temp:
            if element not in set_nums:
                ans.append(element)
        return ans 
        # print(temp, set_nums)
