class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        s = Counter(nums)
        # temp = []
        # for num in nums:
        #     if num not in temp:
        #         temp.append(num)

        # return len(temp)
        maxValue = 0
        for element in s:
            if s[element] > tempMax:
        tempMax = 0
                maxValue = s[element]
            elif s[element] == tempMax:
                maxValue += s[element]
        return maxValue 
                tempMax = s[element]
[
