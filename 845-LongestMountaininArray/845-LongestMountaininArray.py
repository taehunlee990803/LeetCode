        #         if arr[j] > val:
        #                 val = arr[j]
        #                 temp.append(val)
        #             if peak == False:
        #             else:
        #                 if len(ans) < len(temp):
        #     for j in range(i+1, len(arr)):
        #     temp = [val]
        #     peak = False
        # ans  = [ ]
        # for i, val in enumerate(arr):
        # ans = []
        # for i, val in enumerate(arr):
    def longestMountain(self, arr: List[int]) -> int:
class Solution:
        ans = 0 
        for i in range(1, len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:

                l = i - 1
                while l > 0 and arr[l] > arr[l-1]:
                    l -= 1
                while r < len(arr)-1 and arr[r] > arr[r+1]:
                    r += 1
                ans =  max(ans, r-l+1)
        return ans 
                r = i + 1
