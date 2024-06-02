        while l < len(arr)-k:
            if currentSum >= temp:
                count += 1
            currentSum += arr[l+k]
            currentSum -= arr[l]
        currentSum = sum(arr[l:l+k])
            l += 1

        if currentSum >= temp:
                count += 1
        return count 

        count = 0
        l = 0
        currentSum = sum(arr[l:l+k])
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        temp = threshold*k
class Solution:
[
