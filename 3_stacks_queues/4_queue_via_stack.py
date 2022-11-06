from lib import Stack


class MyQueue():
    def __init__(self):
        self.stacks = [Stack(), Stack()]

    def __shift(self):
        if self.stacks[1].is_empty():
            while not self.stacks[0].is_empty():
                self.stacks[1].push(self.stacks[0].pop())

    def is_empty(self):
        return self.stacks[0].is_empty() and self.stacks[1].is_empty()

    def peek(self):
        self.__shift()

        return self.stacks[1].peek()

    def add(self, data):
        self.stacks[0].push(data)

    def remove(self):
        self.__shift()

        return self.stacks[1].pop()

    def __str__(self):
        return f"Stack 1: {str(self.stacks[0])}, Stack 2: {str(self.stacks[1])}"


queue = MyQueue()

queue.add(1)
queue.add(2)
queue.add(3)
queue.add(4)
assert queue.peek() == 1
assert queue.remove() == 1
assert queue.remove() == 2
queue.add(5)
assert queue.peek() == 3
