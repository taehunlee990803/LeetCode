            #         r1 = intervals[i][0]
            #         l2 = ans[j][1]
            #         l1= ans[j][0]
            #     if temp <= ans[j][1]:
            # for j in range(len(ans)):
                l2 = ans[-1][1]
                r1 = intervals[i][0]
                r2 = intervals[i][1]
                low = min(l1,r1)
                high = max(l2, r2)
                ans[-1] = [low,high]
                # check = True
                # break


            else:
                ans.append(intervals[i])
            #         r2 = intervals[i][1]
                l1= ans[-1][0]
            if ans[-1][-1] >= intervals[i][0]:
            check = False
            temp = intervals[i][0]
        
        for i in range(1, len(intervals)):
        ans = [intervals[0]]
        intervals.sort()
        i = 0
      
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
class Solution:
[[1,3],[2,6],[8,10],[15,18]]
