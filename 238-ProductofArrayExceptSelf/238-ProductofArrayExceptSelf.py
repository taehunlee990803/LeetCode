class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        for element in nums:
          
        total_int = 1
            if element != 0:
        if zeroCount == 0:
                total_int = total_int*element
            
        zeroCount = 0
            else:
                zeroCount += 1
        if zeroCount >= 2:
            return ans

            for i in range(0,len(nums)):
                    ans[i] = total_int//nums[i]    
            return ans
        elif zeroCount == 1:
            for i,j in enumerate(nums):
            return ans

                    if j != 0:
                        ans[i] = 0
                    else:
                        ans[i] = total_int
      
[
