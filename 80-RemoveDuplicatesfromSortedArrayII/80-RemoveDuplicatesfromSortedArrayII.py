        p1 = 1
        p2 = 2

        while p2 < len(nums):
            if nums[p1] == nums[p1-1] and nums[p2] == nums[p2-1] == nums[p2-2]:
                while p2 < len(nums) and nums[p2] == nums[p2-1]:
                    p2+=1
                if p2 == len(nums):
                    break
            p1+=1
            nums[p1] = nums[p2]
            p2+=1
        return p1+1
        # k = 0
[1,1,1,2,2,3]
