from collections import deque
class MinStack:
    def __init__(self):
        self.stack = deque()
        self.minstack = deque()
    def push(self,val: int ) -> None:
        self.stack.append(val)
        val = min(val,self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)

    def pop(self):
        return self.stack.pop()
        return self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]

s = MinStack()
s.push(-2)
s.push(-3)
s.push(0)
value = s.getMin()
print(value)