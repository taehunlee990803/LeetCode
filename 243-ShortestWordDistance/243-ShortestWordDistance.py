            if wordsDict[i] == word1:
                word1_container.append(i)
            if wordsDict[i] == word2:
                word2_container.append(i)

                
        for i in range(len(word1_container)):
        ans = float('inf')
            for j in range(len(word2_container)):
                temp = abs(word2_container[j]-word1_container[i])
                ans = min(ans, temp)
        return ans 
[
