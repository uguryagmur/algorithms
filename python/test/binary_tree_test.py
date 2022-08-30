from turtle import pos
from algorithms.tree.binary_tree import Node as BTNode
from algorithms.tree.binary_search_tree import Node as BSTNode
from typing import List


def test_node_creation():
    node = BTNode(4)
    assert node._data == 4
    assert node.left is None
    assert node.right is None

    node = BTNode(4, BTNode(1), BTNode(2))
    assert node._data == 4
    assert node.left._data == 1
    assert node.right._data == 2


def test_get_degree():
    node = BTNode(4)
    assert node.getDegree() == 0
    node.right = BTNode(3)
    assert node.getDegree() == 1
    node.left = BTNode(2)
    assert node.getDegree() == 2
    node.right = None
    assert node.getDegree() == 1


def test_get_height():
    tree = BTNode(5, BTNode(3, BTNode(1, BTNode(0)), BTNode(4)))
    assert tree.getHeight() == 3
    assert tree.left.getHeight() == 2
    assert tree.left.left.getHeight() == 1
    assert tree.left.right.getHeight() == 0
    assert tree.left.left.left.getHeight() == 0


def test_node_in_order_traverse():
    tree = BTNode(5, BTNode(3, BTNode(1), BTNode(4)), BTNode(7, BTNode(6), BTNode(8)))
    assert tree.traverse_in_order() == [1, 3, 4, 5, 6, 7, 8]


def test_node_pre_order_traverse():
    tree = BTNode(5, BTNode(3, BTNode(1), BTNode(4)), BTNode(7, BTNode(6), BTNode(8)))
    assert tree.traverse_pre_order() == [5, 3, 1, 4, 7, 6, 8]


def test_node_post_order_traverse():
    tree = BTNode(5, BTNode(3, BTNode(1), BTNode(4)), BTNode(7, BTNode(6), BTNode(8)))
    assert tree.traverse_post_order() == [1, 4, 3, 6, 8, 7, 5]


def test_binary_tree_creation_with_in_and_pre_order_traversals():
    in_order_traversal: List[int] = [7, 6, 9, 3, 4, 5, 8, 2, 1]
    pre_order_traversal: List[int] = [4, 7, 9, 6, 3, 2, 5, 8, 1]
    post_order_traversal: List[int] = [6, 3, 9, 7, 8, 5, 1, 2, 4]

    tree: BTNode = BTNode.create_from_pre_and_in_order_traversals(
        in_order_traversal, pre_order_traversal
    )
    assert tree.traverse_in_order() == in_order_traversal
    assert tree.traverse_pre_order() == pre_order_traversal
    assert tree.traverse_post_order() == post_order_traversal


def test_binary_tree_creation_with_in_and_pre_order_traversals():
    in_order_traversal: List[int] = [7, 6, 9, 3, 4, 5, 8, 2, 1]
    pre_order_traversal: List[int] = [4, 7, 9, 6, 3, 2, 5, 8, 1]
    post_order_traversal: List[int] = [6, 3, 9, 7, 8, 5, 1, 2, 4]

    tree: BTNode = BTNode.create_from_post_and_in_order_traversals(
        in_order_traversal, post_order_traversal
    )

    assert tree.traverse_in_order() == in_order_traversal
    assert tree.traverse_pre_order() == pre_order_traversal
    assert tree.traverse_post_order() == post_order_traversal


def test_binary_search_tree_creation_with_insertion_array():
    insertion_array: List[int] = [5, 3, 7, 1, 4, 6, 8]

    tree = BSTNode.create_with_insertion_array(insertion_array)

    assert tree.traverse_in_order() == [1, 3, 4, 5, 6, 7, 8]
    assert tree.traverse_pre_order() == [5, 3, 1, 4, 7, 6, 8]
    assert tree.traverse_post_order() == [1, 4, 3, 6, 8, 7, 5]


def test_binary_search_tree_creation_with_pre_order_traversal():
    pre_order_traversal: List[int] = [5, 3, 1, 4, 7, 6, 8]

    tree = BSTNode.create_with_pre_order_traversal(pre_order_traversal)

    assert tree.traverse_in_order() == [1, 3, 4, 5, 6, 7, 8]
    assert tree.traverse_pre_order() == [5, 3, 1, 4, 7, 6, 8]
    assert tree.traverse_post_order() == [1, 4, 3, 6, 8, 7, 5]
