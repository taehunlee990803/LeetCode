        #     for i in word:
        #         if i not in dic:
        #             dic[i] = 1
        #         else:
        # dic = {}
        # for word in words:
        for i in words:
            res &= Counter(i)
            # print(list(res.elements()))
        return list(res.elements())
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = Counter(words[0])
        print(res)
[
