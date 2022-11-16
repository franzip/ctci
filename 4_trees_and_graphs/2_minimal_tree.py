from lib import BinarySearchTree
from typing import List


def tree_from_list(list: List[int]):
    """
    Given a sorted listed, creates a BST with the minimal possible height
    """
    result = BinarySearchTree()

    def __build_tree(list):
        length = len(list)

        if length == 1:
            result.add(list[0])
            return
        if length == 2:
            result.add(list[1])
            result.add(list[0])
            return

        mid = length // 2

        result.add(list[mid])
        __build_tree(list[0:mid])
        __build_tree(list[mid + 1:])

    __build_tree(list)

    return result


assert tree_from_list([1]).get_height() == 1
assert tree_from_list([1, 2, 3]).get_height() == 2
assert tree_from_list([10, 20, 35, 43, 45, 65, 97]).get_height() == 3
assert tree_from_list(
    [10, 20, 35, 43, 45, 65, 97, 100]).get_height() == 4
