from collections import namedtuple


class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinaryTree():
    def __init__(self):
        self.head = None
        self.count = 0

    def add(self, data):
        if not self.head:
            self.head = TreeNode(data)
        else:
            self.__add_to(self.head, data)

    def pre_order_traversal(self):
        self.__traverse('pre_order')

    def in_order_traversal(self):
        self.__traverse('in_order')

    def post_order_traversal(self):
        self.__traverse('post_order')

    def get_height(self):
        return self.__get_height(self.head)

    def print_tree(self, space=0):
        self.__print_tree(self.head, space)

    def __add_to(self, node, data):
        queue = [node]
        while len(queue):
            item = queue[0]
            queue.pop(0)

            if not item.left:
                item.left = TreeNode(data)
                break
            else:
                queue.append(item.left)

            if not item.right:
                item.right = TreeNode(data)
                break
            else:
                queue.append(item.right)

    def __traverse_in_order(self, node: TreeNode, fn=print):
        if node:
            self.__traverse_in_order(node.left)
            fn(node)
            self.__traverse_in_order(node.right)

    def __traverse_pre_order(self, node: TreeNode, fn=print):
        if node:
            fn(node)
            self.__traverse_pre_order(node.left)
            self.__traverse_pre_order(node.right)

    def __traverse_post_order(self, node: TreeNode, fn=print):
        if node:
            self.__traverse_post_order(node.left)
            self.__traverse_post_order(node.right)
            fn(node)

    def __traverse(self, strategy='in_order', fn=print):
        if strategy == 'in_order':
            self.__traverse_in_order(self.head, fn)

        elif strategy == 'pre_order':
            self.__traverse_pre_order(self.head, fn)

        elif strategy == 'post_order':
            self.__traverse_post_order(self.head, fn)

    def __print_tree(self, node, space):
        if (node == None):
            return

        space += 10

        self.__print_tree(node.right, space)

        print()
        for i in range(10, space):
            print(end=" ")
        print(node.data)

        self.__print_tree(node.left, space)

    def __get_height(self, node):
        if node is None:
            return 0

        left_depth = self.__get_height(node.left)
        right_depth = self.__get_height(node.right)

        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1


class BinarySearchTree(BinaryTree):
    def __add_to(self, node, data):
        if data < node.data:
            if node.left:
                self.__add_to(node.left, data)
            else:
                node.left = TreeNode(data)
                self.count += 1
        else:
            if node.right:
                self.__add_to(node.right, data)
            else:
                node.right = TreeNode(data)
                self.count += 1


# https://github.com/somacdivad/graph-theory-with-python
class Graph:
    def __init__(self, nodes, edges, is_directed=True):
        self.graph = namedtuple(
            "Graph", ['nodes', 'edges'])(nodes, edges)
        self.is_directed = is_directed

    def get_adjacency_dict(self):
        adj = {node: [] for node in self.graph.nodes}

        for edge in self.graph.edges:
            node1, node2 = edge[0], edge[1]
            adj[node1].append(node2)

            if not self.is_directed:
                adj[node2].append(node1)
        return adj

    def __str__(self):
        return str(self.get_adjacency_dict())

    def __repr__(self):
        return str(self)


class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

        def __str__(self):
            return f"[{self.data}]"

        def __eq__(self, other):
            return self.data == other.data

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = nodes.pop(0)
            if not isinstance(node, self.Node):
                node = self.Node(data=node)
            self.head = node
            for elem in nodes:
                node.next = self.Node(data=elem) if not isinstance(
                    elem, self.Node) else elem
                node = node.next

    def __str__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(f"{node}")
            node = node.next
        nodes.append("End")
        return " -> ".join(nodes)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        this_head = self.head
        other_head = other.head

        while this_head.next and other_head.next:
            if this_head != other_head:
                return False
            this_head = this_head.next
            other_head = other_head.next

        return this_head.next == None and other_head.next == None
