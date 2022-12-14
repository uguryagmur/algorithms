from abc import ABC
from turtle import left
from typing import Optional


class NodeAbstract(ABC):
    def __init__(
        self,
        data,
        left_child: Optional["NodeAbstract"] = None,
        right_child: Optional["NodeAbstract"] = None,
    ) -> None:
        self._data = data
        self.left = left_child
        self.right = right_child

    def getDegree(self) -> int:
        if self.left is None and self.right is None:
            return 0
        elif self.left is None or self.right is None:
            return 1
        else:
            return 2

    def getHeight(self) -> int:
        left_degree: int = self.left.getHeight() + 1 if self.left else 0
        right_degree: int = self.left.getHeight() + 1 if self.right else 0
        return max(left_degree, right_degree)

    def traverse_in_order(self, traverse_list: Optional[list] = None) -> list:
        if traverse_list is None:
            traverse_list: list = list()

        if self.left is not None:
            self.left.traverse_in_order(traverse_list)
        traverse_list.append(self._data)
        if self.right is not None:
            self.right.traverse_in_order(traverse_list)
        return traverse_list

    def traverse_pre_order(self, traverse_list: Optional[list] = None) -> list:
        if traverse_list is None:
            traverse_list: list = list()

        traverse_list.append(self._data)
        if self.left is not None:
            self.left.traverse_pre_order(traverse_list)
        if self.right is not None:
            self.right.traverse_pre_order(traverse_list)
        return traverse_list

    def traverse_post_order(self, traverse_list: Optional[list] = None) -> list:
        if traverse_list is None:
            traverse_list: list = list()

        if self.left is not None:
            self.left.traverse_post_order(traverse_list)
        if self.right is not None:
            self.right.traverse_post_order(traverse_list)
        traverse_list.append(self._data)
        return traverse_list
