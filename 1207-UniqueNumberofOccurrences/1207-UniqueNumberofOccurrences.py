











class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num = []


        count = Counter(arr)
        for element in count:
            if count[element] not in num:
                num.append(count[element])
            else:
                return False
        return True 
