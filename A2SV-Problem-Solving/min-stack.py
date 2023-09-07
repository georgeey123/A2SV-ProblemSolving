class MinStack:

    def __init__(self):
        self.stack = []
        self.min_size = None
        self.size = 0

    def push(self, val: int) -> None:
        if self.size == 0:
            self.stack.append(val)
            self.min_size = val
        else:
            if val >= self.min_size:
                self.stack.append(val)
            else:
                self.stack.append((2 * val) - self.min_size)
                self.min_size = val
        self.size += 1

        # return self.min_size

    def pop(self) -> None:
        if not self.stack:
            return
        x = self.stack.pop()
        
        if x < self.min_size:
            self.min_size = (2 * self.min_size) - x

        self.size -= 1

    def top(self) -> int:
        if not self.stack:
            return

        x = self.stack[-1]
        if x >= self.min_size:
            return x
        return self.min_size

    def getMin(self) -> int:
        return self.min_size
 

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()