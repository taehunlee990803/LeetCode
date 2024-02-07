class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""
        count = Counter(s)
        sorted_s = dict( sorted(count.items(), key=operator.itemgetter(1), reverse=True))

        for element in sorted_s:

            for j in range(sorted_s[element]):
                ans += element
        return ans
"
