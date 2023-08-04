class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
         
        potions.sort()
        return [len(potions) - bisect_left(potions, (success + a - 1) // a) for a in spells]

        # potions.sort()
        # ans = []
        # for spell in spells:
        #     print(success/spell)
        #     index = bisect_left(potions, success/spell)
        #     print("--",index)
        #     ans.append(len(potions) - index)
        # return ans
#         ans = []
#         count = 0
#         new_potion = sorted(potions, reverse = True)
#         length_potions = len(potions)
        
#         for element in spells:
#             count = 0
#             temp = (success-1)//element
        
#             for element2 in new_potion: #5,4,3,2,1
#                 if element2 >= temp:
#                     count+=1
#                 else:
#                     break
                
#             ans.append(count)
            
#         return ans
