# A native stack for HVM
from collections import deque

class Stack(deque):
    push = deque.append

    def top(self):
        return self[-1]
    
    def negate(self):
        self.push(-self.pop())
    
    def add(self):
        self.push(self.pop() + self.pop())
    
    def minus(self):
        last = self.pop()
        self.push(self.pop() - last)
    
    def mul(self):
        self.push(self.pop() * self.pop())

    def div(self):
        last = self.pop()
        self.push(self.pop() / last)

    def mod(self):
        last = self.pop()
        self.push(self.pop() % last)
    
    def dup(self):
        self.push(self.top())