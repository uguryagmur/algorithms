pub mod binary_search_tree;
pub mod binary_tree;
mod tests {
    mod test_binary_tree;
}

fn main() {
    let bst = binary_search_tree::Node::create_from_insertion_array([5, 3, 7, 1, 4, 6, 8].to_vec());
    println!("Binary Search Tree Pre Order Traversal -> {:?}", bst.traverse_pre_order());
    println!("Binary Search Tree In Order Traversal -> {:?}", bst.traverse_in_order());
}
