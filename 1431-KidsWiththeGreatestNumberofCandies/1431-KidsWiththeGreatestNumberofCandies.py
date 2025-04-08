class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans= []*len(candies)












        maxCandies = max(candies)
        for candy in candies:
            if candy + extraCandies >= maxCandies:
                ans.append(True)
            else:
                ans.append(False)
        return ans 
