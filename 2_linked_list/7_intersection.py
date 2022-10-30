from lib import LinkedList, Node


def intersection(list1: LinkedList, list2: LinkedList):
    """
    Find and return an intersection node between list1 and list2
    """
    refs, ptr1, ptr2 = set(), list1.head, list2.head

    while ptr1 or ptr2:
        if ptr1:
            ref = id(ptr1)
            if ref in refs:
                return ptr1
            refs.add(ref)
            ptr1 = ptr1.next
        if ptr2:
            ref = id(ptr2)
            if ref in refs:
                return ptr2
            refs.add(ref)
            ptr2 = ptr2.next

    return None


node = Node(1)

assert intersection(LinkedList([2, 3, node, 4, 5]),
                    LinkedList([5, 4, 15, 3, node])) == node
assert intersection(LinkedList([1, 2, 3, 4]),
                    LinkedList([1, 2, 3, 4])) == None
