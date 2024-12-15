                if nums[l] <= target:
                    r = m - 1
                else:
                    l = m + 1
        return -1
            
            

                

            elif nums[m] > target:
                    l = m + 1
                else:
                    r = m - 1
                if nums[l] >= target:
            elif nums[m] < target:
                return m
            if nums[m] == target:
            m = (l+r)//2
        while l<=r :
