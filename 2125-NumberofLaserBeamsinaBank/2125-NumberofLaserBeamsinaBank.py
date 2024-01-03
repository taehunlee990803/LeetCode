class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = 0
        height = len(bank)
        container = []
        width = len(bank[0])
        for i in range(0,height):
            temp = 0
            for j in range(0,width):
                if int(bank[i][j]) == 1:
                    temp+=1
            
        
        for i in range(0,len(container)-1):
            count += container[i]*container[i+1]
            if temp != 0:
                container.append(temp)
        return count

["011001","000000","010100","001000"]
