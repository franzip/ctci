from lib import LinkedList


def remove_dups(list: LinkedList):
    """
    Removes duplicates from a singly linked list
    """
    curr = list.head

    while curr:
        runner = curr

        while runner.next:
            if runner.next == curr:
                runner.next = runner.next.next
            else:
                runner = runner.next
        curr = curr.next


a = LinkedList([2, 2, 5, 10, 2, 3, 10, 5])
remove_dups(a)
assert a == LinkedList([2, 5, 10, 3])

b = LinkedList([2, 3, 4, 5, 6])
remove_dups(b)
assert b == LinkedList([2, 3, 4, 5, 6])
