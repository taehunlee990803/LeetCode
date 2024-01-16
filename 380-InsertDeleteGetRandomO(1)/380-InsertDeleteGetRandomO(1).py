        

    def remove(self, val: int) -> bool:
        if val in self.st:
        self.st.add(val)
        return True
            self.st.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        

        return random.choice(tuple(self.st))
[
