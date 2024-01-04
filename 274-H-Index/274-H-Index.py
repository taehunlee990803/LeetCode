        #     return 1
        # # total = len(citations)
        # maxValue = 0
        #     return 0
        # if citations[0] == 0 and total == 1:
        #     return 0 
        # if total == 1:
        # print(citations)
        # total = len(citations)
        # if citations[0] == 0 and total == 0:
#01356
#01234
#54321
        citations.sort()
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        total = len(citations)
        for i,v in enumerate(citations):
            if total - i <= v:
                print(total-i,v)
                return total-i
        return 0
[3,0,6,1,5]
