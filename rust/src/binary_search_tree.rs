use std::path;

#[path = "./binary_tree.rs"]
mod binary_tree;

pub struct Node<T: Copy> {
    _data: T,
    _left: Option<Box<Node<T>>>,
    _right: Option<Box<Node<T>>>,
}

impl<T: Copy + std::cmp::PartialEq> Node<T> {
    pub fn create(data: T, left: Option<Box<Node<T>>>, right: Option<Box<Node<T>>>) -> Node<T> {
        Self {
            _data: data,
            _left: left,
            _right: right,
        }
    }

    pub fn get_data(&self) -> &T {
        &self._data
    }

    pub fn get_left_child(&self) -> Option<&Box<Node<T>>> {
        self._left.as_ref()
    }

    pub fn get_right_child(&self) -> Option<&Box<Node<T>>> {
        self._right.as_ref()
    }

    pub fn set_data(&mut self, data: T) {
        self._data = data;
    }

    pub fn traverse_in_order(&self) -> Vec<T> {
        let mut traverse_data: Vec<T> = Vec::new();
        if self._left.is_some() {
            self.get_left_child()
                .unwrap()
                ._traverse_in_order(&mut traverse_data);
        }
        traverse_data.push(self._data);
        if self._right.is_some() {
            self.get_right_child()
                .unwrap()
                ._traverse_in_order(&mut traverse_data);
        }
        traverse_data
    }

    pub fn traverse_pre_order(&self) -> Vec<T> {
        let mut traverse_data: Vec<T> = Vec::new();
        traverse_data.push(self._data);
        if self._left.is_some() {
            self.get_left_child()
                .unwrap()
                ._traverse_pre_order(&mut traverse_data);
        }
        if self._right.is_some() {
            self.get_right_child()
                .unwrap()
                ._traverse_pre_order(&mut traverse_data);
        }
        traverse_data
    }

    pub fn traverse_post_order(&self) -> Vec<T> {
        let mut traverse_data: Vec<T> = Vec::new();
        if self._left.is_some() {
            self.get_left_child()
                .unwrap()
                ._traverse_post_order(&mut traverse_data);
        }
        if self._right.is_some() {
            self.get_right_child()
                .unwrap()
                ._traverse_post_order(&mut traverse_data);
        }
        traverse_data.push(self._data);
        traverse_data
    }

    fn _traverse_in_order(&self, traverse_data: &mut Vec<T>) {
        if self._left.is_some() {
            self.get_left_child()
                .unwrap()
                ._traverse_in_order(traverse_data);
        }
        traverse_data.push(self._data);
        if self._right.is_some() {
            self.get_right_child()
                .unwrap()
                ._traverse_in_order(traverse_data);
        }
    }

    fn _traverse_pre_order(&self, traverse_data: &mut Vec<T>) {
        traverse_data.push(self._data);
        if self._left.is_some() {
            self.get_left_child()
                .unwrap()
                ._traverse_pre_order(traverse_data);
        }
        if self._right.is_some() {
            self.get_right_child()
                .unwrap()
                ._traverse_pre_order(traverse_data);
        }
    }

    fn _traverse_post_order(&self, traverse_data: &mut Vec<T>) {
        if self._left.is_some() {
            self.get_left_child()
                .unwrap()
                ._traverse_post_order(traverse_data);
        }
        if self._right.is_some() {
            self.get_right_child()
                .unwrap()
                ._traverse_post_order(traverse_data);
        }
        traverse_data.push(self._data);
    }
}

impl<T: Copy + std::cmp::PartialEq + std::cmp::PartialOrd> Node<T> {

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
        } else if self._data < *data {
            if self._left.is_none() {
                self._left = Some(Box::new(Node::create(*data, None, None)));
            } else {
                self._left.as_mut().unwrap().insert(data);
            }
        } else {
            if self._right.is_none() {
                self._right = Some(Box::new(Node::create(*data, None, None)))
            } else {
                self._right.as_mut().unwrap().insert(data);
            }
        }
    }
}
