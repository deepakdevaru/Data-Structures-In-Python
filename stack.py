class stack:
    def __init__(self):
        self.stack = []

    def isempty(self):
        return self.stack == []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        data = self.stack[-1]
        return data

    def size_stack(self):
        return len(self.stack)


stack = stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print (stack.stack)

