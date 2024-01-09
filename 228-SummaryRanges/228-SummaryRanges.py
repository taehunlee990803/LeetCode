class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = [[nums[0]]]
        for i in range(1, len(nums)):
            value = nums[i]
            temp = ans[-1][-1]
            if temp + 1 == value:
                ans[-1].append(value)
            else:
                ans.append([value])
        print(ans)
        for element in ans:
            if len(element) == 1:
        final = []
                final.append(str(element[0]))
            else:
                container = ""
                container+=str(element[-1])
                final.append(container)
                container+=str(element[0])
                container+="->"
        if len(nums) == 0:
            return ""
        return final
[0,1,2,4,5,7]
