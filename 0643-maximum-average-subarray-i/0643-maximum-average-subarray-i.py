class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_average = 0
        average = 0
        length = len(nums)
        
        max_sum = sum(nums[:k])
        s = max_sum
        for i in range(1,length-k+1):
            s -= nums[i-1] # sum - nums[0]
            s += nums[i+k-1] # sum + nums[4]
            max_sum = max(s, max_sum)
        return max_sum/float(k)
        
#         if length == 1:
#             return nums[0]
#         else:
#             for i in range(0,length-k+1):
#                 sum = 0
#                 print("i:",i)
#                 for j in range(i,i+k):
#                     sum += nums[j]
#                 temp_average = sum/float(k)
#                 print(temp_average)
#                 max_average = max(temp_average, max_average)
#         # elif length == 2:
#         #     return (nums[0]+nums[1])/2.0
#         # elif length == 3:
#         #     return (nums[0]+nums[1]+nums[2])/3.0
            
#         return max_average
    
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         s=sum(nums[:k])
#         m=s
#         for i in range(1,len(nums)-k+1):
#             s-=nums[i-1]
#             s+=nums[i+k-1]
#             m=max(m, s)
#         return m/k