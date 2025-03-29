        #     if len(ans) == 0:
        #         ans.append(element)
        #         ans.append([])
        #     else:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1) # left branch

            subset.pop()
            # decision to include nums[i]
            dfs(i+1)
        dfs(0)
        return res

