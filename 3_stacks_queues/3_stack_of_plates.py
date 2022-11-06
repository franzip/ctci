from lib import Stack, StackEmptyException


class StackFullException(Exception):
    pass


class StackWithCapacity(Stack):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity

    def is_full(self):
        return len(self.data) >= self.capacity

    def push(self, data):
        if self.is_full():
            raise StackFullException()

        super().push(data)


class StackOfPlates():
    def __init__(self, capacity=5):
        self.stacks = []
        self.capacity = capacity

    def __extend_stack(self, data):
        new_stack = StackWithCapacity(self.capacity)
        new_stack.push(data)
        self.stacks.append(new_stack)

    def peek(self):
        if self.is_empty():
            raise StackEmptyException()

        return self.stacks[0].peek()

    def is_empty(self):
        return not len(self.stacks)

    def push(self, data):
        if self.is_empty():
            self.__extend_stack(data)
        else:
            last_stack = self.stacks[-1]
            try:
                last_stack.push(data)
            except StackFullException:
                self.__extend_stack(data)

    def pop(self):
        if self.is_empty():
            raise StackEmptyException()

        last_stack = self.stacks[-1]

        item = last_stack.pop()

        if last_stack.is_empty():
            self.stacks.pop()

        return item

    def pop_at(self, index):
        if index > len(self.stacks):
            raise Exception('Stack does not exist')

        stack = self.stacks[index]
        item = stack.pop()

        if stack.is_empty():
            self.stacks = self.stacks[0:index] + self.stacks[index+1:]

        return item

    def __str__(self):
        return str([str(stack) for stack in self.stacks])


stack = StackOfPlates(5)

stack.push(21)
stack.push(11)
stack.push(5)
stack.push(9)
stack.push(4)
stack.push(33)
stack.push(50)
stack.push(500)
stack.push(150)
stack.push(350)
stack.push(100)
stack.push(105)
# ['[4, 9, 5, 11, 21]', '[350, 150, 500, 50, 33]', '[105, 100]']
assert stack.pop() == 105
stack.pop_at(1)
stack.pop_at(0)
stack.pop_at(1)
stack.pop_at(0)
stack.pop_at(1)
stack.pop_at(0)
stack.pop_at(1)
stack.pop_at(0)
stack.pop_at(1)
# ['[21]', '[100]']
assert stack.pop() == 100
assert stack.pop() == 21
assert stack.is_empty() == True
