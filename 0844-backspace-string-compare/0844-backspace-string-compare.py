class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def build(s):
            ans = []
            for char in s:
                if char !='#':
                    ans.append(char)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(s) == build(t)
    
    
    
#         new_arr1 = []
#         new_arr2 = []
        
#         if s[0] != '#':
#             new_arr1.append(s[0])
#         if t[0] != '#':
#             new_arr2.append(t[0])
        
#         for i in range(1,len(s)):
#             if s[i] == '#':
#                 if len(new_arr1) != 0:
#                      new_arr1.remove(new_arr1[-1])
#             elif s[i] != '#':
#                 new_arr1.append(s[i])
                
#         for i in range(1,len(t)):
#             if t[i] == '#'and len(new_arr2) != 0:
#                 new_arr2.remove(new_arr2[-1])
#             elif t[i] != '#':
#                 new_arr2.append(t[i])
                
#         print(new_arr1)
            
#         print("-------------")
        
        
#         print(new_arr2)
                                                   
# #         for i in range(0,len(s)):
# #             if s[i] == '#' and s[i-1] == '#':
# #                 new_arr1.remove(new_arr1[-1])
             
# #             if s[i] != '#' and i+1 == len(s):
              
# #                 new_arr1.append(s[i])
# #             elif s[i+1] =='#' and i+1 != len(s):
# #                 i+=1
               
# #             elif s[i+1] != '#' and s[i] != '#':
             
# #                 new_arr1.append(s[i])
                
# #         for i in range(0,len(t)):
# #             if t[i] == '#' and t[i-1] == '#':
# #                 new_arr2.remove(new_arr2[-1])
             
# #             if t[i] != '#' and i+1 == len(t):
              
# #                 new_arr2.append(t[i])
# #             elif t[i+1] =='#' and i+1 !=len(t):
# #                 i+=1
               
# #             elif t[i+1] != '#' and t[i] != '#':
             
# #                 new_arr2.append(t[i])  
              
# #         for i in range(0,len(new_arr1)):
# #             print(new_arr1[i])
            
# #         print("-------------------")
        
# #         for i in range(0,len(new_arr2)):
# #             print(new_arr2[i])
# #         for i in range(0,len(t)):
# #             if t[i+1] != '#' and i+1 ! = len(s):
# #                 new_arr2.append(t[i])
                                
#         if len(new_arr1) != len(new_arr2):
#             return False
#         else:
#             for i in range(0,len(new_arr1)):
#                 if new_arr1[i] != new_arr2[i]:
#                     return False
#             return True
    
        