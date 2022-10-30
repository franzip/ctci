class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"[{self.data}]"

    def __eq__(self, other):
        return self.data == other.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = nodes.pop(0)
            if not isinstance(node, Node):
                node = Node(data=node)
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem) if not isinstance(
                    elem, Node) else elem
                node = node.next

    def __str__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(f"{node}")
            node = node.next
        nodes.append("End")
        return " -> ".join(nodes)

    def __eq__(self, other):
        this_head = self.head
        other_head = other.head

        while this_head.next and other_head.next:
            if this_head != other_head:
                return False
            this_head = this_head.next
            other_head = other_head.next

        return this_head.next == None and other_head.next == None
