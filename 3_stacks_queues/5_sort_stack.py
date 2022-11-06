from lib import Stack


def sort_stack(stack: Stack):
    if stack.is_empty():
        return

    def __sort(input_stack: Stack, sorted_stack: Stack, current):
        if sorted_stack.is_empty():
            sorted_stack.push(current)
            return __sort(input_stack, sorted_stack, input_stack.pop())

        if current < sorted_stack.peek():
            input_stack.push(sorted_stack.pop())
            __sort(input_stack, sorted_stack, current)
        else:
            sorted_stack.push(current)
            if input_stack.is_empty():
                while not sorted_stack.is_empty():
                    input_stack.push(sorted_stack.pop())

                return
            __sort(input_stack, sorted_stack, input_stack.pop())

    return __sort(stack, Stack(), stack.pop())


stack = Stack()


stack.push(5)
stack.push(10)
stack.push(3)
stack.push(25)
stack.push(1)
stack.push(7)
sort_stack(stack)
assert stack.pop() == 1
assert stack.pop() == 3
assert stack.pop() == 5
assert stack.pop() == 7
assert stack.pop() == 10
assert stack.pop() == 25
