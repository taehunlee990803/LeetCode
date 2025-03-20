class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # dic = dict()
        # for element in nums:
        #     if element not in dic:
        #         dic[element] = 1
        #     else:
        #         dic[element] += 1
        # for element in dic:
        #     if dic[element] == 1:
        #         return element

        result = 0
        for num in nums:
            result ^= num
            print(num, result)
        return result
