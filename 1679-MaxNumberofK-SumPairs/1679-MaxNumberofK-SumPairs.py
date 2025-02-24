        nums.sort()
        l = 0
        r = len(nums)-1
        ans = 0

        while l < r:
            temp = nums[l] + nums[r]
            if temp == k:
                l += 1
                r -= 1
                ans += 1
            else:
                if temp <= k:
                    l += 1
                else:
                    r -=1 
        return ans 


