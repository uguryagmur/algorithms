from algorithms.tree.binary_tree_abstract import NodeAbstract
from typing import List


class Node(NodeAbstract):
    @classmethod
    def create_with_insertion_array(cls, insertion_data: list) -> "Node":
        root: Node = Node(insertion_data[0])
        for i in range(1, len(insertion_data)):
            root.insert(insertion_data[i])

        return root

    @classmethod
    def create_with_pre_order_traversal(cls, pre_order_traversal: list) -> "Node":
        root = Node(pre_order_traversal[0])
        left_pre_order: List[Node] = [
            e for e in pre_order_traversal if pre_order_traversal[0] > e
        ]
        right_pre_order: List[Node] = [
            e for e in pre_order_traversal if pre_order_traversal[0] < e
        ]

        if left_pre_order:
            root.left = Node.create_with_pre_order_traversal(left_pre_order)

        if right_pre_order:
            root.right = Node.create_with_pre_order_traversal(right_pre_order)

        return root

    def insert(self, data):
        if self._data < data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        elif self._data > data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            raise Exception("AlreadyFoundError: data is already in the tree")
