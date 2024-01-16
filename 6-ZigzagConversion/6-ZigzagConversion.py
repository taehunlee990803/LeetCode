                index += 1
                if index == numRows:
                    asc = False
                    index -= 2
            else:
                ans[index].append(s[count])
                index -= 1
                if index == -1:
                    asc = True
                ans[index].append(s[count])
        asc = True
        count = 0
        while count < len(s):
            # print(count, index)
            if asc:
        ans = []
        for i in range(numRows):
            ans.append([])        
        index = 0
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
"
