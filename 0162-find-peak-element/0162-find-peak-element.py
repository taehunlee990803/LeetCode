class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ans_index = []
        length = len(nums)
        
        if length == 1:
            return 0
        elif length == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        count = 0
            
        for i in range(0,length-1):
            if i == 0:
                if nums[1] < nums[0]:
                    ans_index.append(0)
            elif i == length-2 and nums[i] < nums[i+1]:
                ans_index.append(i+1)
            elif nums[i-1]<nums[i] and nums[i]>nums[i+1]:
                ans_index.append(i)
                if i == length-2 and nums[i] < nums[i+1]:
                    ans_index.append(i+1)
                    print("@")

        print(ans_index)
                
        return ans_index[0]