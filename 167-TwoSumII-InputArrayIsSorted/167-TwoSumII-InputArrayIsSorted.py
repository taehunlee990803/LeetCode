        # while l != r:
        #     if numbers[l] + numbers[r] == target:
        #         return [l+1, r+1]
        # r = len(numbers) -1
        # l = 0
        # ans = []
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
class Solution:
        dic = {}
        for i, num in enumerate(numbers):
            temp = target - num
        return [1,1]
            if temp in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i
[
0
