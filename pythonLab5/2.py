class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop(0)

    def peek(self):
        if not self.items:
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

queue: Queue = Queue()

for i in range(3):
    queue.push(i+1)

print(queue.pop())
print(queue.peek())

for i in range(3):
    print(queue.pop())
