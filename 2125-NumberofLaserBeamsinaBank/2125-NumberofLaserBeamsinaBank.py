        # for i in range(0,len(container)-1):
        #     count += container[i]*container[i+1]
        # return count
        # count = 0
        # for i in range(0,height):
        # temp = 0
        #     for j in range(0,width):
        #         if int(bank[i][j]) == 1:
        #     temp = 0
        #             temp+=1
        #     if zero == 0:
        # zero = 0
        #         zero = temp
        #     else:
        #         if temp != 0:
        #             count += zero*temp
        #             zero = temp
        # return count 
        #             print(zero, temp)


        ans = prev = 0
        for s in bank:
            c = s.count('1')
            if c:
                ans += prev*c
                prev = c
        return ans 
            
["011001","000000","010100","001000"]
