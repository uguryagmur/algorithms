pub struct Node<T: Copy> {
    _data: T,
    _left: Option<Box<Node<T>>>,
    _right: Option<Box<Node<T>>>,
}

impl<T: Copy + std::cmp::PartialEq + std::fmt::Debug> Node<T> {
    pub fn create(data: T, left: Option<Box<Node<T>>>, right: Option<Box<Node<T>>>) -> Node<T> {
        Self {
            _data: data,
            _left: left,
            _right: right,
        }
    }

    pub fn create_binary_tree_from_pre_and_in_order_traversals(
        pre_order: &[T],
        in_order: &[T],
    ) -> Node<T> {
        assert_eq!(
            pre_order.len(),
            in_order.len(),
            "Given traversals are not correct !"
        );
        if pre_order.len() == 1 {
            return Node::create(pre_order[0], None, None);
        }

        let index = in_order.iter().position(|&x| x == pre_order[0]).unwrap();
        let left_in_order = &in_order[0..index];
        let right_in_order = &in_order[index + 1..];

        let left_pre_order = &pre_order[1..1 + left_in_order.len()];
        let right_pre_order = &pre_order[1 + left_in_order.len()..];

        let left: Option<Box<Node<T>>> = if left_in_order.is_empty() {
            None
        } else {
            Some(Box::new(
                Node::create_binary_tree_from_pre_and_in_order_traversals(
                    left_pre_order,
                    left_in_order,
                ),
            ))
        };

        let right: Option<Box<Node<T>>> = if right_in_order.is_empty() {
            None
        } else {
            Some(Box::new(
                Node::create_binary_tree_from_pre_and_in_order_traversals(
                    right_pre_order,
                    right_in_order,
                ),
            ))
        };

        Node::create(pre_order[0], left, right)
    }

    pub fn create_binary_tree_from_post_and_in_order_traversals(
        post_order: &[T],
        in_order: &[T],
    ) -> Node<T> {
        assert_eq!(post_order.len(), in_order.len());
        if post_order.len() == 1 {
            return Node::create(post_order[0], None, None);
        }

        let index = in_order
            .iter()
            .position(|&x| x == post_order[post_order.len() - 1])
            .unwrap();
        let left_in_order = &in_order[0..index];
        let right_in_order = &in_order[index + 1..];

        let right_post_order =
            &post_order[post_order.len() - right_in_order.len() - 1..post_order.len() - 1];
        let left_post_order = &post_order[0..post_order.len() - right_in_order.len() - 1];

        let left: Option<Box<Node<T>>> = if left_in_order.is_empty() {
            None
        } else {
            Some(Box::new(
                Node::create_binary_tree_from_post_and_in_order_traversals(
                    left_post_order,
                    left_in_order,
                ),
            ))
        };

        let right: Option<Box<Node<T>>> = if right_in_order.is_empty() {
            None
        } else {
            Some(Box::new(
                Node::create_binary_tree_from_post_and_in_order_traversals(
                    right_post_order,
                    right_in_order,
                ),
            ))
        };

        Node::create(post_order[post_order.len() - 1], left, right)
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
