class MyQueue:

    def __init__(self):
        self.s2 = []

    def push(self, x: int) -> None:

    def pop(self) -> int:
        

    def peek(self) -> int:
        

    def empty(self) -> bool:
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)

        self.s1 = []
        return self.s1[-1]
        return len(self.s1) == 0

        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
        return self.s1.pop()
[
