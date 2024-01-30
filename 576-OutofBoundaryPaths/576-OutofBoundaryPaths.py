class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        container = []
        dic = {}

        for element in mat:
            count = 0
            for i in range(len(element)):
                if element[i] == 1:
                    count += 1
            dic[temp] = count
        temp = 0
            temp+=1
        sorted_dic = dict(sorted(dic.items(), key=lambda key_val: key_val[1]))
        # print(dic)
        return key_list[:k]
                else:
                    break
        key_list = list(sorted_dic.keys())
        # return ans
[
