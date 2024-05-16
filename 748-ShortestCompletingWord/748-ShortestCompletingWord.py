        for word in words:
            if len(word) < tc:
            for char in word:
                if char in t and t[char] > 0:
            t = dic.copy()
                continue
                    t[char] -= 1
            tcc = tc
                tc += 1
                    dic[element] = 1
                else:
                    dic[element] += 1
            if element.isalpha():
                if element not in dic:
        for element in licensePlate:
                    tcc -= 1
            if tcc == 0:
                return word
        words = sorted(words, key = lambda word:len(word))
        print(dic)
        return ""

                    
"
