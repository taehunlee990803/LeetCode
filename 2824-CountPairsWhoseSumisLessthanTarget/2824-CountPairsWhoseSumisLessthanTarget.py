class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # l = 0
        # r = len(nums)-1
        # count = 0
        # for i in range(0,len(nums)):
        #     first = i
        #     r = len(nums)-1
        #     while first < r:
        #         sum_value = nums[first] + nums[r]
        #         if sum_value < target:
        #             count += 1
               
        #         r -= 1
                   
        # return count 
        #             print(first,r)
        nums.sort()
        count = 0
        l = 0
        r = len(nums)-1

        while l < r:
            if nums[l] + nums[r] < target:
                count += l - r
                l+=1
            else:
                r-=1
        return count 
[
