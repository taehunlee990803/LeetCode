        for i in range(len(spells)):
            # temp = []
            count = 0
            l = 0
            r = len(potions)
            while l < r:
                mid = (l+r)//2
                current = spells[i] * potions[mid]
                if current >= success:
                else:

                    r = mid
                    l = mid + 1
                
            ans.append(n-l)
        n = len(potions)
        potions.sort()
        ans = []
success: int) -> List[int]:
    def successfulPairs(self, spells: List[int], potions: List[int], 
            
class Solution:
