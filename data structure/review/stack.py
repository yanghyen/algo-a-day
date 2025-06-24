# pop, peek 구현

class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self):
        return len(self.top) == 0
    
    def size(self):
        return len(self.top)
    
    def clear(self):
        self.top = []

    def push(self, item):
        self.top.append(item)

    def pop(self):
        pass
    
    def peek(self):
        pass