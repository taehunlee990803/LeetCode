        #     return ans
        # else:
        temp = ""
        for element in title:
            if element == " ":
        container = []
                container.append(temp)
        ans = ""
                temp = ""
            else:
                temp += element
        for i in range(len(container)):
            if len(container[i]) > 2:
                for j in range(len(container[i])):
                    if j == 0:
                        ans += container[i][0].upper()
                    else:
                        ans += container[i][j].lower()
            else:
                for j in range(len(container[i])):
                    ans += container[i][j].lower()
            if i is not len(container) - 1:
                ans += " "
        container.append(temp)
        #             ans+= chr(element)
"
