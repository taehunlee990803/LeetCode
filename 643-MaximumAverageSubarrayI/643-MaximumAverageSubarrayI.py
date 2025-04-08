
    def findMaxAverage(self, nums: List[int], k: int) -> float:

class Solution:

        for i in range(1, len(nums)-k+1):
            currentSum -= nums[i-1]
        return maxAverage 
            # currentAverage = 
        # # len(nums) == 5
            # print(i)
            maxAverage = max(maxAverage, currentSum / k)
        currentSum = sum(nums[:k])

    
        maxAverage = currentSum/k



            currentSum += nums[k+i-1]

        # 0,1,1,3,3
        # i = 0 -> 0 + 1 + 2 + 3 - currentSum
        # i = 1 -> currentSum - nums[0] + nums[4]
