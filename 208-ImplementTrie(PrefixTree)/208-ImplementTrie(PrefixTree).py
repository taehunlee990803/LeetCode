    def insert(self, word: str) -> None:
        

    def search(self, word: str) -> bool:
        self.dic.add(word)
        for i in range(len(word)):
            self.prefix.add(word[:i+1])
        return word in self.dic

    def startsWith(self, prefix: str) -> bool:
        


# Your Trie object will be instantiated and called as such:
        return prefix in self.prefix
[
