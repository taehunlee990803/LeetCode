        points.sort()
        prev = points[0]
        for i in range(1,len(points)):

            curr = points[i]
            if curr[0] <= prev[1]: # [1,5], [2,6]
                res -= 1
                prev = [curr[0], min(prev[1], curr[1])]
        
            else:
                prev = curr
        return res
        
