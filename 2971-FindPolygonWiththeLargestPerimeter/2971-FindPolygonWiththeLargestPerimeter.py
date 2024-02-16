class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        maxNum = -1
        for i in range(len(nums)-1,1,-1):
            current = nums[i]

            currentSum = sum(nums[:i])
            if currentSum > current:
                # maxNum = max(maxNum, currentSum + current)
            
                return currentSum + current
        return maxNum
[
