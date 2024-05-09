        temp = sorted(happiness)

        
        for i in range(k):
        dec = 0
        length = len(happiness)
            current =  temp[length-1-dec]
                ans += current
            if current-dec >= 0:
                current -= dec
            else:
            dec +=1
                return ans                
        return ans 
        
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans = 0
class Solution:
[
