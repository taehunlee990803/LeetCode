        words = sentence.split()
        for word in words:
            prefix = set()
            for i in range(len(word)):
                prefix.add(word[:i+1])
        ans = []
            check = 0

        # print(dic)
        # print(prefix)
        # prefix = sorted(prefix)
            for t in prefix:
                if t in dictionary:
                    ans.append(t)
            prefix= sorted(prefix)
                    check = 1
                    break
            if check == 0:
                ans.append(word)
        return ' '.join(ans)
            
[
