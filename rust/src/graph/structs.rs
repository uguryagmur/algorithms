use std::collections::HashMap;

#[derive(Eq, Clone, Copy, Hash, PartialEq, Debug)]
pub struct GraphNode<T> {
    pub _id: usize,
    pub _data: T,
}

pub struct UndirectedGraph<T> {
    pub _adj_list: HashMap<GraphNode<T>, Vec<GraphNode<T>>>,
}

pub struct DirectedGraph<T> {
    pub _adj_list: HashMap<GraphNode<T>, Vec<GraphNode<T>>>,
}
