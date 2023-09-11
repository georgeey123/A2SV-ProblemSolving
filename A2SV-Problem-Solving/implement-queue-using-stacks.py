class MyQueue:

    def __init__(self):
        self.in_queue = []
        self.out_queue = []

    def push(self, x: int) -> None:
        self.in_queue.append(x)

    def pop(self) -> int:
        if not self.out_queue:
            self.fill()

        return self.out_queue.pop()


    def peek(self) -> int:
        if not self.out_queue:
            self.fill()

        top = self.out_queue.pop()
        self.out_queue.append(top)
        return top

    def empty(self) -> bool:
        return not len(self.out_queue) and not len(self.in_queue)

    def fill(self):
        while self.in_queue:
            self.out_queue.append(self.in_queue.pop())
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()