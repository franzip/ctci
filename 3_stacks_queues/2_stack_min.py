from lib import Stack


class StackMin(Stack):
    def __init__(self):
        super().__init__()
        self.mins = Stack()

    def push(self, data):
        if self.mins.is_empty() or data < self.mins.peek():
            self.mins.push(data)

        super().push(data)

    def pop(self):
        item = super().pop()
        if item == self.mins.peek():
            self.mins.pop()
        return item

    def min(self):
        try:
            return self.mins.peek()
        except:
            return None

    def __str__(self):
        try:
            return f"{super(self).__str__()}\nMin: {self.mins.peek()}"
        except:
            return str(super)


stack = StackMin()
stack.push(10)
stack.push(5)
stack.push(7)
stack.push(15)
stack.push(3)
assert stack.min() == 3
stack.push(1)
assert stack.min() == 1
stack.pop()
assert stack.min() == 3
stack.pop()
stack.pop()
assert stack.min() == 5
stack.pop()
assert stack.min() == 5
stack.pop()
assert stack.min() == 10
