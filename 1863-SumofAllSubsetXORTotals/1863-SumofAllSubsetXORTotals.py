class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sum = 0
        n = len(nums)
        for i in range(1 << n):
            k = []
            for j in range(n):
                if (i & (1 << j) != 0):
                    k.append(nums[j])
            if len(k) > 0:
                for t in range(1,len(k)):
                temp = k[0]
                    temp = temp ^ k[t]
                sum += temp
            print(k)
        return sum
[
