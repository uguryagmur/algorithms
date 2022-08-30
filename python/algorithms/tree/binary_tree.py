from algorithms.tree.binary_tree_abstract import NodeAbstract


class Node(NodeAbstract):
    @classmethod
    def create_from_pre_and_in_order_traversals(
        cls, in_order_traversal: list, pre_order_traversal: list
    ) -> "Node":
        assert len(in_order_traversal) == len(
            pre_order_traversal
        ), "Tree traversal arrays are not correct"
        if not in_order_traversal or not pre_order_traversal:
            raise Exception("Traversal arrays cannot be empty")

        node = Node(pre_order_traversal[0])

        index: int = in_order_traversal.index(pre_order_traversal[0])
        left_in_order_traversal: list = in_order_traversal[:index]
        right_in_order_traversal: list = in_order_traversal[index + 1 :]

        left_pre_order_traversal: list = pre_order_traversal[
            1 : 1 + len(left_in_order_traversal)
        ]
        right_pre_order_traversal: list = pre_order_traversal[
            1 + len(left_in_order_traversal) :
        ]

        if left_in_order_traversal and left_pre_order_traversal:
            node.left = Node.create_from_pre_and_in_order_traversals(
                left_in_order_traversal, left_pre_order_traversal
            )
        if right_in_order_traversal and right_pre_order_traversal:
            node.right = Node.create_from_pre_and_in_order_traversals(
                right_in_order_traversal, right_pre_order_traversal
            )

        return node

    @classmethod
    def create_from_post_and_in_order_traversals(
        cls, in_order_traversal: list, post_order_traversal: list
    ) -> "Node":
        assert len(in_order_traversal) == len(
            post_order_traversal
        ), "Tree traversal arrays are not correct"
        if not in_order_traversal or not post_order_traversal:
            raise Exception("Traversal arrays cannot be empty")
        node = Node(post_order_traversal[-1])

        index: int = in_order_traversal.index(post_order_traversal[-1])
        left_in_order_traversal: list = in_order_traversal[:index]
        right_in_order_traversal: list = in_order_traversal[index + 1 :]

        left_post_order_traversal: list = post_order_traversal[
            : len(left_in_order_traversal)
        ]
        right_post_order_traversal: list = post_order_traversal[
            len(left_in_order_traversal) : -1
        ]

        if left_in_order_traversal and left_post_order_traversal:
            node.left = cls.create_from_post_and_in_order_traversals(
                left_in_order_traversal, left_post_order_traversal
            )

        if right_in_order_traversal and right_post_order_traversal:
            node.right = cls.create_from_post_and_in_order_traversals(
                right_in_order_traversal, right_post_order_traversal
            )

        return node
