        # dict_container = {}
        # index = 0
        # for element in strs:
        #     temp = str(element)
        #     temp_sorted = ''.join(sorted(temp))
        #     if temp_sorted not in dict_container:
        #         dict_container[temp_sorted] = index
        #         arr.append([element])
        #         index += 1
        #     else:
        #         k = dict_container[temp_sorted]
        # arr = []
        anagram_map = defaultdict(list)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        return list(anagram_map.values())
["eat","tea","tan","ate","nat","bat"]
[""]
["a"]
