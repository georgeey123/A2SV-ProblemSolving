class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyStack:

    def __init__(self):
        self.stack = None
        self.size = 0

    def push(self, x: int) -> None:
        node = Node(x)

        if not self.stack:
            self.stack = node
            return
        head = self.stack

        node.next = head
        self.stack = node
        self.size += 1

    def pop(self) -> int:
        # temp = self.stack[-1]
        if not self.stack:
            return
        
        temp = self.stack.val

        self.stack = self.stack.next
        # self.stack.next = None

        self.size -= 1
        return temp


    def top(self) -> int:
        if not self.stack:
            return

        return self.stack.val
        # cur = cur.next

        # temp = self.stack[-1]
        # return temp

    def empty(self) -> bool:
        if not self.stack:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()