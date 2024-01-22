                dic[temp] = [ num ]
            else:
                dic[temp].append(num)
            if temp in dic:
          
                # container.append(temp)
            # if temp not in container:
        # print(dic)
        i = 0
        sorted_dic = dict(sorted(dic.items(), key=lambda x: x[0], reverse=True))
        # container.sort(reverse = True)
        print(dic)
        for element in sorted_dic:
            dic[element].sort(reverse = True)
            for j in range(len(dic[element])):
                ans.append(dic[element][j])
            temp = abs(num - median)

        for num in arr:
        # container = []
[
