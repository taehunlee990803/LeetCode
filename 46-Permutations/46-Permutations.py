        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)

            perms = self.permute(nums) # perms = [[2,3], [3,2]]

            nums.append(n)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
        return res

        res = []
    def permute(self, nums: List[int]) -> List[List[int]]:
class Solution:
