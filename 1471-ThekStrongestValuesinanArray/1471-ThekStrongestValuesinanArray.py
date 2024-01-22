        #         if i == k:
        #             return ans 
        # return ans 
        arr.sort()
        mid = arr[(len(arr)-1)//2]
        ans = []
        l,r = 0, len(arr)-1
        while l <= r:
            if abs(arr[l]-mid) > abs(arr[r]-mid):
                ans.append(arr[l])
                l+=1
            else:
                ans.append(arr[r])
                r-=1
            if len(ans) == k:
        return ans
                return ans      
[
