pub struct Node<T: Copy> {
    _data: T,
    _left: Option<Box<Node<T>>>,
    _right: Option<Box<Node<T>>>,
}

impl<T: Copy> Node<T> {
    pub fn new(data: T, left: Option<Box<Node<T>>>, right: Option<Box<Node<T>>>) -> Node<T> {
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
        traverse_data.push(self._data);
        if self._left.is_some() {
            self.get_left_child()
                .unwrap()
                ._traverse_in_order(&mut traverse_data);
        }
        if self._right.is_some() {
            self.get_right_child()
                .unwrap()
                ._traverse_in_order(&mut traverse_data);
        }
        traverse_data
    }

    pub fn traverse_pre_order(&self) -> Vec<T> {
        let mut traverse_data: Vec<T> = Vec::new();
        if self._left.is_some() {
            self.get_left_child()
                .unwrap()
                ._traverse_pre_order(&mut traverse_data);
        }
        traverse_data.push(self._data);
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
        traverse_data.push(self._data);
        if self._left.is_some() {
            self.get_left_child()
                .unwrap()
                ._traverse_in_order(traverse_data);
        }
        if self._right.is_some() {
            self.get_right_child()
                .unwrap()
                ._traverse_in_order(traverse_data);
        }
    }

    fn _traverse_pre_order(&self, traverse_data: &mut Vec<T>) {
        if self._left.is_some() {
            self.get_left_child()
                .unwrap()
                ._traverse_pre_order(traverse_data);
        }
        traverse_data.push(self._data);
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
