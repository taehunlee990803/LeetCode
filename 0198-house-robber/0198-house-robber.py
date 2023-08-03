class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])
        
        dp = [0]*length
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        
        for i in range(2,length):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            
        print(dp)    
        return max(dp)
        
#          dp[i] = max(dp[i-2]+nums[i], dp[i-1])
#         if len(nums) < 3:
#             return max(nums[0],nums[1])
        
#         dp = [0 for _ in range(len(nums))]
        
#         dp[0] = nums[0]
        
#         for i in range(1,len(nums)):
#             dp[i] = nums[i] + dp[i+2]
            
#         return max(dp[-1],dp[-2]) 
    
    
#         class Solution(object):
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         length = len(nums)
#         if length==0:
#             return 0
#         if length==1:
#             return nums[0]
#         if length==2:
#             return max(nums)
			
#         dp = [0]*length # assign dp array
#         dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
#         for i in range(2, length):
#             dp[i] = max(dp[i-2]+nums[i], dp[i-1])
#         print(dp)
        
#         return max(dp)