        #     if i <= k:
        #         count += min(tickets[k], tickets[i])
        #     else:
        #         count += min(tickets[k]-1, tickets[i])
        # return count 
        time = 0
        while True:
            for i in range(len(tickets)):
                if tickets[k] == 0:
                    return time
                if tickets[i] >= 1:
                    tickets[i] -= 1
        # for i in range(len(tickets)):
        # count = 0
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
class Solution:
