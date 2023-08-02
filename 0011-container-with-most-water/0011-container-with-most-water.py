
class Solution(object):
    def maxArea(self, height):
        L = 0
        R = len(height) - 1
        width = len(height) -1
        res = 0

        for w in range(width, 0, -1):
            if height[L] < height[R]:
                res = max(res, height[L]*w)
                L = L+1
            else:
                res = max(res,height[R]*w)
                R = R-1
        return res
        
        

# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         max_area = 0
#         area = 0
#         length = len(height)
#         diff = 0
        
#         for i in range(0,length):
#             for j in range(i+1, length):
#                 max_area = max((j-i) * min(height[i],height[j]),max_area)

                
        
#         return max_area
        
        
#         for i in range(0,length):
#             for j in range(i+1,length):
#                 diff = height[i] - height[j]
            
#                 if diff > 0:
#                     area = diff*diff
#                     if area > max_area:
#                         max_area = area
                    
                    
#         return max_area