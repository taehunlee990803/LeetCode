            else:
                dic[element] = 1
                container.append(element)
            if element in dic:
                k = dic[element]
                for i in range(k):
                    ans.append(element)
        for element in container:
        container = sorted(container)
        for element in arr2:
                container.remove(element)
            k = dic[element]
            for i in range(k):
                ans.append(element)

        return ans 
[
