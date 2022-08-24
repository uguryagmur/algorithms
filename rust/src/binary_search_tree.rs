#[path = "./binary_tree.rs"]
mod binary_tree;

pub struct Node<T: Copy + std::fmt::Display> {
    _data: T,
    _left: Option<Box<Node<T>>>,
    _right: Option<Box<Node<T>>>,
}

use binary_tree::implement_binary_tree_attributes;
implement_binary_tree_attributes!(Node);

impl<T: Copy + std::cmp::PartialEq + std::cmp::PartialOrd + std::fmt::Display> Node<T> {
    pub fn create_from_insertion_array(array: Vec<T>) -> Self {
        let mut root = Node::create(array[0], None, None);
        for i in 1..array.len() {
            root.insert(&array[i]);
        }
        root
    }

    pub fn insert(&mut self, data: &T) {
        if self._data == *data {
            panic!("Given data is already in the tree");
        } else if self._data > *data {
            if self._left.is_none() {
                println!("current node is {}", self._data);
                println!("next created node on left is {}", data);
                println!("-------------------");
                self._left = Some(Box::new(Node::create(*data, None, None)));
            } else {
                self._left.as_mut().unwrap().insert(data);
            }
        } else {
            if self._right.is_none() {
                println!("current node is {}", self._data);
                println!("next created node on right is {}", data);
                println!("-------------------");
                self._right = Some(Box::new(Node::create(*data, None, None)))
            } else {
                self._right.as_mut().unwrap().insert(data);
            }
        }
    }
}
