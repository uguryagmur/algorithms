#[cfg(test)]
mod tests {
    use crate::binary_search_tree::Node;

    #[test]
    fn test_node_set_data() {
        let mut node = Node::create(33, None, None);
        node.set_data(64);
        assert_eq!(node.get_data(), &64);
    }

    #[test]
    fn test_tree_creation_with_insertion_array() {
        let insertion_vector = [5, 3, 7, 1, 4, 6, 8].to_vec();
        let tree = Node::create_from_insertion_array(insertion_vector);
        assert_eq!([5, 3, 1, 4, 7, 6, 8].to_vec(), tree.traverse_pre_order());
        assert_eq!([1, 3, 4, 5, 6, 7, 8].to_vec(), tree.traverse_in_order());
    }
}
