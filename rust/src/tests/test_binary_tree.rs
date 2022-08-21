#[cfg(test)]
mod tests {
    use crate::binary_tree::Node;

    #[test]
    fn test_node_set_data() {
        let mut node = Node::new(33, None, None);
        node.set_data(64);
        assert_eq!(node.get_data(), &64);
    }
}
