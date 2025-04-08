                    temp += s[i]
                    i += 1
                container.append(temp)
            else:
                i += 1
        print(container)
        ans = ""
        for i in range(len(container)-1,-1,-1):
            if i != 0:
                ans += container[i]
                ans += " "
            else:
                    # print(i, container,temp)
                while i < len(s) and s[i] != " ":
                temp = ""
            if s[i] != " ":
        # for i in range(len(s)):
        while i < len(s):
        i = 0
                ans += container[i]
        return ans 
    
            
