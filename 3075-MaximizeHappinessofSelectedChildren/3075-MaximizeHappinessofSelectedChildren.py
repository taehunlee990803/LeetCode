        # for i in range(k):
        #     current =  temp[length-1-dec]
        #     if current-dec >= 0:
        #         current -= dec


            i += 1
            k -= 1
        return ans 
        while k > 0:
            ans += max(happiness[i]-i,0)
        dec = 0
        i = 0

        ans = 0
        happiness.sort(reverse = True)
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
[
