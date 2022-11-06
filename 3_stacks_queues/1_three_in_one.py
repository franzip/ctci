class MultiStack():
    def __init__(self, size):
        self.size = size
        self.data = [None for x in range(self.size)]
        self.stack_size = len(self.data) // self.size

    def is_empty(self, stack_num):
        if stack_num >= self.size:
            raise Exception("Invalid stack number")

        return not self.data[stack_num * self.stack_size]

    def peek(self, stack_num):
        if stack_num >= self.size:
            raise Exception("Invalid stack number")

        item = self.data[stack_num * self.stack_size]

        if not item:
            raise Exception('Empty stack')

        return item

    def push(self, data, stack_num):
        if stack_num >= self.size:
            raise Exception("Invalid stack number")

        offset = stack_num * self.stack_size
        max_offset = offset + self.stack_size

        if not self.data[offset]:
            self.data[offset] = data
        else:
            while offset < len(self.data) and self.data[offset]:
                offset += 1

        if offset > max_offset:
            self.__resize()
            self.data[max_offset] = data
        else:
            self.data[offset] = data

    def pop(self, stack_num):
        if stack_num >= self.size:
            raise Exception("Invalid stack number")

        idx = stack_num * self.stack_size
        item = self.data[idx]
        if not item:
            raise Exception('Empty stack')

        while self.data[idx]:
            self.data[idx] = self.data[idx + 1]
            idx += 1

        return item

    def __resize(self):
        next_size = len(self.data) * self.size
        tail = [None for x in range(next_size - self.stack_size)]
        new_stack_data = []
        for i in range(self.size):
            offset = i * self.stack_size
            new_stack_data += self.data[offset:offset +
                                        self.stack_size] + tail

        self.data = new_stack_data
        self.stack_size = next_size

    def print_stack(self, stack_num):
        if stack_num >= self.size:
            raise Exception("Invalid stack number")
        return str([val for val in self.data[stack_num * self.stack_size:stack_num * self.stack_size + self.stack_size]])

    def __str__(self):
        return str([[self.data[j] for j in range(i * self.stack_size, i * self.stack_size + self.stack_size)]
                    for i in range(self.size)])


multistack = MultiStack(3)

multistack.push(3, 0)
multistack.push(4, 1)
multistack.push(5, 2)
multistack.push(5, 0)
multistack.push(6, 0)
multistack.push(6, 0)
multistack.push(6, 2)
multistack.push(1, 2)
assert multistack.pop(2) == 5
assert multistack.pop(2) == 6
assert multistack.pop(2) == 1

try:
    multistack.pop(2)
except Exception as e:
    assert str(e) == 'Empty stack'
