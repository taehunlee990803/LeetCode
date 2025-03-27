                    tmp.append(a+c.lower())
                    tmp.append(a+c.upper())
                    # print("tmp: ", tmp)
                    # print("------")
            else:
                for a in ans:
                    tmp.append(a+c)
            ans = tmp
            if c.isalpha():
                for a in ans:
                    # print("------")
                    # print("a in ans", a, ans)
            tmp = []
            # print("C: ", c)
        for c in s:
            # print("Current Output: ", ans)
            
        return ans 

                  
