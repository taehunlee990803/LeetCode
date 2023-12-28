class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic = Counter(nums)
        ans = set()
        nums.sort()
        for i in range(0,len(nums)):
            # for j in range(i+1, len(nums)):
            #     temp = nums[i] + nums[j]
              
            #     temp_minus = temp*-1

            #     if nums[j+1] > temp_minus:
            #         break
            second = i + 1
            while second < last:
                temp = nums[first] + nums[second] + nums[last]
            last = len(nums) -1
                if temp == 0:

                    ans.add((nums[first], nums[second], nums[last]))
                    second += 1
                    last -= 1
                elif temp > 0:
                    last -= 1
                else:
                    second += 1
        return ans

            first = i
[
