class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self): return len(self.queue) == 0

    def enqueue(self, n):
        self.queue.append(n)
        print(f"Enqueued Data: {n}")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        
        n = self.queue.pop()
        print(f"Dequeued Data: {n}")

    def display(self):
        if self.isEmpty(): 
            print("Queue is Empty")
        else:
            print(f"Queue: {self.queue}")

q = Queue()

q.enqueue(14)
q.enqueue(8)
q.enqueue(4)

q.display()

q.dequeue()
q.dequeue()

q.display()