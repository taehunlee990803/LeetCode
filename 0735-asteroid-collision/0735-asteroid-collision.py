class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        prev = asteroids[0]
        ans = []
        
        for element in asteroids:
            while ans and element < 0 < ans[-1]:
                if abs(element) > abs(ans[-1]):
                    ans.pop()
                elif element + ans[-1] == 0:
                    ans.pop()
                    break
                else:
                    break
            else:
                ans.append(element)
        
        return ans
            
    
    
#     class Solution:
#     def asteroidCollision(self, asteroids):
#         stack = []
#         for asteroid in asteroids:
#             while stack and asteroid < 0 < stack[-1]:
#                 if stack[-1] < -asteroid:
#                     stack.pop()
#                     continue
#                 elif stack[-1] == -asteroid:
#                     stack.pop()
#                 break
#             else:
#                 stack.append(asteroid)
#         return stack
    
    
#     if len(ans) == 0:
#                 ans.append(element)
#             else:
#                 ans_element = ans[-1]
                
                
#                 while element * ans_element < 0:
#                     ans_element = ans[-1]
#                     if ans_element + element == 0:
#                          ans.remove(ans_element)
                         
#                     elif abs(ans_element) < abs(element):
#                         ans.remove(ans_element)
#                         if 
#                         ans.append(element)
                
#                 ans.append(element)
                
                
                
                
                
#                 if ans_element * element < 0:
#                     if ans_element + element == 0:
#                          ans.remove(ans_element)
#                     elif abs(ans_element) < abs(element):
#                         ans.remove(ans_element)
#                         if 
#                         ans.append(element)
#                 else:
#                     ans.append(element)
#         return ans
    
#     class Solution(object):
#     def asteroidCollision(self, asteroids):
#         stack = []

#         for i in asteroids:
#             while stack and i < 0 and stack[-1] > 0:
#                 if abs(i) > stack[-1]:
#                     stack.pop()
#                 elif abs(i) == stack[-1]:
#                     stack.pop()
#                     break
#                 else:
#                     break
#             else:
#                 stack.append(i)

#         return stack