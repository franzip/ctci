from lib import LinkedList, Node


def delete_node_from_list(node: Node):
    """
    Removes a node from the middle of a singly linked list
    """
    if not node or not node.next:
        return

    next_node = node.next
    node.data = next_node.data
    node.next = next_node.next


nodeA = Node(10)
a = LinkedList([2, 5, 10, nodeA, 3, 10, 5])
delete_node_from_list(nodeA)
assert a == LinkedList([2, 5, 10, 3, 10, 5])

nodeB = Node(6)
b = LinkedList([2, 3, 4, 5, nodeB])
delete_node_from_list(nodeB)
assert b == LinkedList([2, 3, 4, 5, nodeB])
