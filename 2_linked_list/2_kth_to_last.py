from lib import LinkedList, Node


def get_kth_node_to_last(list: LinkedList, k: int) -> Node:
    """
    Returns the k-th node to the last in a singly linked list
    """
    assert k >= 1

    head, nodes, count = list.head, [], 0

    while head:
        nodes.append(head)
        head = head.next
        count += 1

        idx = (count - k)

    return nodes[idx]


assert get_kth_node_to_last(LinkedList([1, 2, 3, 4, 5, 6, 7, 8]), 1) == Node(8)
assert get_kth_node_to_last(LinkedList([1, 2, 3, 4, 5, 6, 7, 8]), 2) == Node(7)
assert get_kth_node_to_last(LinkedList([1, 2, 3, 4, 5, 6, 7, 8]), 5) == Node(4)
