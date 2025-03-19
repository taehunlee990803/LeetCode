            r = len(nums)-1
        
            while l < r:
                tempSum = val + nums[l] + nums[r]
                # print(i, l, r)
                # print( current, nums[l], nums[j])
                # print("sum:", tempSum)
                if tempSum == 0:
                    temp = [val, nums[l], nums[r]]
                    # if sorted(temp) not in ans:
                    #     ans.append(sorted(temp))
                    l += 1
                    # ans.append([current, nums[l], nums[j]])
                    # break
            l = i+1
                continue
            if (i > 0) and val == nums[i-1]:
            # for j in range(i+1, len(nums)):
            
        # for i in range(len(nums)):
         
        # print(nums)
        nums = sorted(nums)
        ans = []
        for i, val in enumerate(nums):
                    while (l < r) and nums[l] == nums[l-1]:
                    # temp.append()
                    ans.append(temp)
