class StackEmptyException(Exception):
    pass


class QueueEmptyException(Exception):
    pass


class Stack():
    def __init__(self):
        self.data = []

    def peek(self):
        if self.is_empty():
            raise StackEmptyException('Empty stack')

        return self.data[0]

    def is_empty(self):
        return not len(self.data)

    def push(self, data):
        if not len(self.data):
            self.data = [data]
        else:
            self.data = [data] + self.data

        return data

    def pop(self):
        if self.is_empty():
            raise StackEmptyException()

        head = self.data[0]
        self.data = self.data[1:]
        return head

    def __str__(self):
        return str(self.data)


class Queue():
    def __init__(self):
        self.data = []

    def is_empty(self):
        return not len(self.data)

    def peek(self):
        if self.is_empty():
            raise QueueEmptyException()

        return self.data[0]

    def add(self, data):
        self.data.append(data)

    def remove(self):
        if self.is_empty():
            raise QueueEmptyException()

        head = self.data[0]
        self.data = self.data[1:]
        return head

    def __str__(self):
        return str(self.data)
