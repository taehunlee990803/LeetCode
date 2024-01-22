class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # length = len(nums)
        # print(nums)
        # prev = nums[0]
        # ans = []
        # nums.sort()
        # dic = Counter(nums)
        # for element in dic:
        #     if dic[element] == 2:
        #         ans.append(element)
        #         nums.remove(element)

        duplicate, missing = -1, -1

        for i in range(1, len(nums)+1):
            count = nums.count(i)
            if count == 2:
                duplicate = i
            elif count == 0:
                missing = i

        return [duplicate, missing]
[
