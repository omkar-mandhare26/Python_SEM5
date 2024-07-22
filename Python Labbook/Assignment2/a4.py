class Stack:
    def __init__(self):
        self.stk = []
    
    def isEmpty(self):
        return (len(self.stk) == 0)

    def push(self, n):
        self.stk.append(n)

    def pop(self):
        if(self.isEmpty()): print("\nList is Empty")
        else:
            n = self.stk.pop()
            return n

    def display(self):
        print("\nList Elements: ")
        for n in self.stk:
            print(n)

    def search(self,n):
        return self.stk.index(n)

stack = Stack()
stack.push(5)
stack.push(7)
stack.push(9)

stack.display()
print(f"Index of 7 in Stack: {stack.search(7)}")


stack.pop()
stack.pop()
stack.display()

stack.pop()
stack.pop()