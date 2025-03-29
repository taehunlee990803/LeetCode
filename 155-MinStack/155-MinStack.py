        # else:
        #     current_min = min(val, self.stack[-1][1])
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:


            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


        self.min_stack.pop()
