class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
            arr = sorted(arr)
            minDiff = arr[1] - arr[0]
            ans = []
            for i in range(1, len(arr)-1):
                diff = arr[i+1] - arr[i]
                if diff < minDiff:
                    minDiff = diff
            for i in range(len(arr)-1):
                diff = arr[i+1] - arr[i]
                if diff == minDiff:
                    ans.append([arr[i], arr[i+1]])

            return ans
