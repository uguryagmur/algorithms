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
        stack: List["Node"] = list()
        stack.append(Node(pre_order_traversal[0]))
        for i in range(1, len(pre_order_traversal)):
            print(f"stack state -> {[node._data for node in stack]}")
            if stack[-1]._data > pre_order_traversal[i]:
                stack[-1].left = Node(pre_order_traversal[i])
                stack.append(stack[-1].left)
            else:
                stack.pop()
                stack[-1].right = Node(pre_order_traversal[i])
                stack.append(stack[-1].right)
        return stack[0]

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
