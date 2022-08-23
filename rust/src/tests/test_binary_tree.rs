#[cfg(test)]
mod tests {
    use crate::binary_tree::Node;

    #[test]
    fn test_node_set_data() {
        let mut node = Node::create(33, None, None);
        node.set_data(64);
        assert_eq!(node.get_data(), &64);
    }

    #[test]
    fn test_node_creation_by_pre_and_in_order_traversals() {
        let pre_order = [4, 7, 9, 6, 3, 2, 5, 8, 1];
        let in_order = [7, 6, 9, 3, 4, 5, 8, 2, 1];
        let tree: Node<i32> =
            Node::create_binary_tree_from_pre_and_in_order_traversals(&pre_order, &in_order);
        assert_eq!(pre_order.to_vec(), tree.traverse_pre_order());
        assert_eq!(in_order.to_vec(), tree.traverse_in_order());
    }

    #[test]
    fn test_node_creation_by_post_and_in_order_traversals() {
        let post_order = [6, 3, 9, 7, 8, 5, 1, 2, 4];
        let in_order = [7, 6, 9, 3, 4, 5, 8, 2, 1];
        let tree: Node<i32> =
            Node::create_binary_tree_from_post_and_in_order_traversals(&post_order, &in_order);
        assert_eq!(in_order.to_vec(), tree.traverse_in_order());
        assert_eq!(post_order.to_vec(), tree.traverse_post_order());
    }
}
