from lib import LinkedList


def partition_list(list: LinkedList, val: int):
    """
    Partition a singly linked list based on a given value
    """
    headLeft, headRight, tailLeft, tailRight = None, None, None, None
    ptr = list.head

    while ptr:
        next = ptr.next
        ptr.next = None

        if ptr.data < val:
            if not headLeft:
                headLeft, tailLeft = ptr, ptr
            else:
                tailLeft.next = ptr
                tailLeft = ptr
        else:
            if not headRight:
                headRight, tailRight = ptr, ptr
            else:
                tailRight.next = ptr
                tailRight = ptr

        ptr = next

    list.head = headLeft
    tailLeft.next = headRight


a = LinkedList([5, 3, 8, 5, 10, 2, 1])
partition_list(a, 5)
assert a == LinkedList([3, 2, 1, 5, 8, 5, 10])

b = LinkedList([3, 5, 8, 5, 10, 2, 1])
partition_list(b, 5)
assert b == LinkedList([3, 2, 1, 5, 8, 5, 10])

c = LinkedList([1, 2, 3, 4, 5, 6])
partition_list(c, 10)
assert c == LinkedList([1, 2, 3, 4, 5, 6])
