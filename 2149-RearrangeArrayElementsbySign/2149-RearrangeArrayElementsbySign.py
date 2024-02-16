class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        positive = []
        negative = []

        for element in nums:
            if element > 0:
                positive.append(element)
            else:
                negative.append(element)

        for i in range(len(nums)//2):
            ans.append(positive[i])
            ans.append(negative[i])
        return ans 
[
