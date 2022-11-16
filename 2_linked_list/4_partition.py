from lib import LinkedList


def partition_list(list: LinkedList, val: int):
    """
    Partition a singly linked list based on a given value
    """
    head_left, head_right, tail_left, tail_right = None, None, None, None
    ptr = list.head

    while ptr:
        next = ptr.next
        ptr.next = None

        if ptr.data < val:
            if not head_left:
                head_left, tail_left = ptr, ptr
            else:
                tail_left.next = ptr
                tail_left = ptr
        else:
            if not head_right:
                head_right, tail_right = ptr, ptr
            else:
                tail_right.next = ptr
                tail_right = ptr

        ptr = next

    list.head = head_left
    tail_left.next = head_right


a = LinkedList([5, 3, 8, 5, 10, 2, 1])
partition_list(a, 5)
assert a == LinkedList([3, 2, 1, 5, 8, 5, 10])

b = LinkedList([3, 5, 8, 5, 10, 2, 1])
partition_list(b, 5)
assert b == LinkedList([3, 2, 1, 5, 8, 5, 10])

c = LinkedList([1, 2, 3, 4, 5, 6])
partition_list(c, 10)
assert c == LinkedList([1, 2, 3, 4, 5, 6])
