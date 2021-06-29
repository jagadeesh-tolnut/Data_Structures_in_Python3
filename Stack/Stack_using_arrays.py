class Stack:
    def __init__(self):
        self.data = []
    def length(self):
        return len(self.data)
    def is_empty(self):
        return len(self.data) == 0
    def push(self,element):
        self.data.append(element)
    def pop(self):
        if self.is_empty():
            pass
        else:
            return self.data.pop()
    def top(self):
        if self.is_empty():
            pass
        else:
            return self.data[-1]

stack = Stack()
print(stack.is_empty())
stack.push(25)
stack.push(50)
stack.push(75)
print(stack.data)
stack.pop()
print(stack.data)
stack.push(100)
stack.push(200)
stack.push(300)
print(stack.data)
stack.top()
print(stack.data)
print(stack.is_empty())
