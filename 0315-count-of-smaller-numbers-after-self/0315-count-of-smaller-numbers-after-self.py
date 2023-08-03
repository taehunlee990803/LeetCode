class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = sorted(nums) #1256
        ans = []
        
#         for num in nums:
#             i = bisect_left(arr,num)    #   <-- 2a)
#             ans.append(i)               #   <-- 2b)
#             del arr[i]                  #   <-- 2c)
            
#         return ans                      #   <-- 3)
        
        
        for num in nums: #5261
            i = bisect_left(arr,num)
            ans.append(i)
            del arr[i] #126 -> 16 
        return ans
    
    
    
    
    
#         length = len(nums)
        
#         if length == 0:
#             return [0]
        
        
        
#         temp_arr = [0]
#         new_arr = [0]*length
#         count = 0
        
#         temp = 0
#         for i in range(0,length-1):
#             count = 0
#             temp = 0
#             temp_arr = [0]*(length-i-1)
#             for j in range(i+1,length):
#                 temp_arr[temp] = nums[j]
#                 temp+=1                
#             temp_arr.sort()
            
#             for element in temp_arr:
#                 if element > nums[i]:
#                     break
#                 elif element < nums[i]:
#                     count+=1
#             new_arr[i] = count
            
#         return new_arr    
