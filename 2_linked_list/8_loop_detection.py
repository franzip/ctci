from lib import LinkedList, Node


def loop_detection(list: LinkedList):
    """
    Find and return the first node triggering a loop
    """
    refs, head = set(), list.head

    while head:
        ref = id(head)

        if ref in refs:
            return head

        refs.add(id(head))
        head = head.next

    return None


node = Node(5)

assert loop_detection(LinkedList(
    [1, 2, 3, 4, node, 6, 7, 8, node])) == node
assert loop_detection(LinkedList([1, 2, 3, 4, 5, 6, 1, 2, 3, 4])) == None
