from lib import BinarySearchTree

tree = BinarySearchTree()

tree.add(8)
tree.add(3)
tree.add(10)
tree.add(2)
tree.add(6)
tree.add(14)
tree.add(9)

tree.print_tree()
print('in_order:')
tree.in_order_traversal()
print('pre_order:')
tree.pre_order_traversal()
print('post_order:')
tree.post_order_traversal()
