class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            for i in range(0,len(nums)):
                if nums[i] == target:
                    return i
        else:
             for i in range(0,len(nums)-1):
                    if nums[i] < target and nums[i+1] > target:
                        return i+1
                
             if target < nums[0]:
                return 0
             if target > nums[len(nums)-1]:
                return len(nums)
           
            
        