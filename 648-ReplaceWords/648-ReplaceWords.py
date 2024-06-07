        # words = sentence.split()
        # ans = []

        # # prefix = sorted(prefix)
        # # print(prefix)
        # # print(dic)
        # prefix = set()
        # dic = set()

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        dictionary = sorted(dictionary)
        for i in range(len(words)):
            for root in dictionary:
                if words[i].startswith(root):
                    words[i] = root
                    break
        return ' '.join(words)

[
