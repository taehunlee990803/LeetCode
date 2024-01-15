class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        temp = candies.copy()
        temp.sort()
        max_candy = temp[-1]
        for element in candies:

        ans = []
            if new >= max_candy:
            else:
                ans.append(False)
                ans.append(True)
            new = element + extraCandies
        
            print(ans)
        return list(ans)
[
