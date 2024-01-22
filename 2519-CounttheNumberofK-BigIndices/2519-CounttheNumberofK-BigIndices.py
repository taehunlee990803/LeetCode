        #     # print(left, right)
        #     if left >= k and right >= k:
        #         current = nums[i]
        #         # print(current)

        #     right = length - i - 1
        # ans = 0
        # for i in range(len(nums)):
        #     left = i

        # length = len(nums)

from sortedcontainers import SortedList
    def kBigIndices(self, nums: List[int], k: int) -> int:
        # if len(nums) <= k:
        #     return 0
        sl1,sl2 = SortedList(),SortedList(nums)
        res = 0
        for i in range(len(nums)):
            sl2.remove(nums[i])
            if sl1.bisect_left(nums[i])>=k and sl2.bisect_left(nums[i])>=k:
                res+=1
            sl1.add(nums[i])
        return res
        #         left_arr = nums[:i]
        #         left_arr.sort()
        #         # print(left_arr, right_arr)
        #         minimum_left = 0
        #         minimum_right = 0
        #         for i in range(len(left_arr)):
        #             if left_arr[i] < current:
        #                 minimum_left += 1
        #             else:
class Solution:

[
0
