class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)
        length = len(candies)

        for i in range(length):
            if candies[i]+extraCandies >= max_num:
        ans = []
                ans.append(True)
            else:
                ans.append(False)
        return ans
