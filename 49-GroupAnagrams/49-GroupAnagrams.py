class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        arr = []
        dict_container = {}
        index = 0
        for element in strs:
            temp = str(element)
            temp_sorted = ''.join(sorted(temp))
            if temp_sorted not in dict_container:
                dict_container[temp_sorted] = index
                arr.append([element])
                index += 1
            else:
                k = dict_container[temp_sorted]
                arr[k].append(element)


          
                # t = len(arr[k])
        return arr
[
