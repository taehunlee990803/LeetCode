        c = list(a-b)
        if len(c) != 0:
            return False
        a_count = Counter(word1)
        b_count = Counter(word2)
        a = []
        b = []

        for element in a_count:
            # if a_count[element] not in a:
            a.append(a_count[element])
        for element in b_count:
            # if b_count[element] not in b:
            b.append(b_count[element])

        a.sort()
        b.sort()
        b = set(word2)
        a = set(word1)
            return False
        if len(word1) != len(word2):
    def closeStrings(self, word1: str, word2: str) -> bool:
class Solution:
            # else:
