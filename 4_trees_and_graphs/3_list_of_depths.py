from lib import BinaryTree, LinkedList


def list_of_depths(tree: BinaryTree):
    """
    Given a binary tree, builds a list of linked lists each representing a tree depth level
    """

    def visit_level(queue, results):
        if not len(queue):
            return results

        results.append(LinkedList(queue[:]))

        next_queue = []

        for node in queue:
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)

        return visit_level(next_queue, results)

    return visit_level([tree.head], [])


tree = BinaryTree()

tree.add(8)
tree.add(3)
tree.add(10)
tree.add(2)
tree.add(6)
tree.add(14)
tree.add(9)

tree.print_tree()
print([list for list in list_of_depths(tree)])
