pub mod binary_tree;
mod tests {
    mod test_binary_tree;
}

fn main() {
    let right = Box::new(binary_tree::Node::create(11, Option::None, Option::None));
    let left = Box::new(binary_tree::Node::create(19, Option::None, Option::None));
    let root = Box::new(binary_tree::Node::create(55, Some(left), Some(right)));
    println!("Root data is {}", root.get_data());
    println!(
        "Left child data is {:?}",
        root.get_left_child().unwrap().get_data()
    );
    println!(
        "Right child data is {}",
        root.get_right_child().unwrap().get_data()
    );
}
