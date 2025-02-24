class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for element in arr:
            if element not in dic:
                dic[element] = 1
            else:
                dic[element] += 1
        for element in dic:
        container = []
    
            count = dic[element]
            if count not in container:
                container.append(count)
            else:
                return False
        return True 

