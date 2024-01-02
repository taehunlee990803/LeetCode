        # container.append(temp)
        # ans = ""

        # for i in range(len(container)):
        #     if len(container[i]) > 2:
        #         for j in range(len(container[i])):
        #             if j == 0:
        #                 ans += container[i][0].upper()
        #             else:
        #                 ans += container[i][j].lower()
        #     else:
        #         for j in range(len(container[i])):
        #             ans += container[i][j].lower()
        #     if i is not len(container) - 1:
        #         ans += " "
        # return ans
        ans = []
        for s in title.split():
            if len(s) <3:
                ans.append(s.lower())
            else:
                ans.append(s.capitalize())
        return ' '.join(ans)
        

"capiTalIze tHe titLe"
"First leTTeR of EACH Word"
"i lOve leetcode"
