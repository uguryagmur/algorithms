use super::structs::*;
use super::traits::Graph;
use std::collections::HashMap;

impl GraphNode<usize> {
    pub fn create_with_id(data: usize) -> Self {
        Self {
            _id: data,
            _data: data,
        }
    }
}

impl<T> GraphNode<T> {
    pub fn create(id: usize, data: T) -> Self {
        Self {
            _id: id,
            _data: data,
        }
    }
}

impl<T> Graph<T> for UndirectedGraph<T>
where
    T: Eq + Copy + std::hash::Hash,
{
    fn new(edges: &[(&GraphNode<T>, &GraphNode<T>)]) -> Self {
        let mut adj_list: HashMap<GraphNode<T>, Vec<GraphNode<T>>> = HashMap::new();
        for edge in edges {
            if adj_list.get(&edge.0).is_none() {
                adj_list.insert(*edge.0, vec![*edge.1]);
            } else {
                adj_list.get_mut(&edge.0).unwrap().push(*edge.1);
            }

            if adj_list.get(&edge.1).is_none() {
                adj_list.insert(*edge.1, vec![*edge.0]);
            } else {
                adj_list.get_mut(&edge.1).unwrap().push(*edge.0);
            }
        }
        Self {
            _adj_list: adj_list,
        }
    }

    fn get_adj_list(&self) -> &HashMap<GraphNode<T>, Vec<GraphNode<T>>> {
        &self._adj_list
    }

    fn add_edge(&mut self, node_1: GraphNode<T>, node_2: GraphNode<T>) {
        self._adj_list.get_mut(&node_1).unwrap().push(node_2);
        self._adj_list.get_mut(&node_2).unwrap().push(node_1);
    }

    fn does_contain_cycle(&self) -> bool {
        false
    }
}

impl<T> Graph<T> for DirectedGraph<T>
where
    T: Eq + Copy + std::hash::Hash,
{
    fn new(edges: &[(&GraphNode<T>, &GraphNode<T>)]) -> Self {
        let mut adj_list: HashMap<GraphNode<T>, Vec<GraphNode<T>>> = HashMap::new();
        for edge in edges {
            if adj_list.get(&edge.0).is_none() {
                adj_list.insert(*edge.0, vec![*edge.1]);
            } else {
                adj_list.get_mut(&edge.0).unwrap().push(*edge.1);
            }

            if adj_list.get(&edge.1).is_none() {
                adj_list.insert(*edge.1, vec![]);
            }
        }
        Self {
            _adj_list: adj_list,
        }
    }

    fn get_adj_list(&self) -> &HashMap<GraphNode<T>, Vec<GraphNode<T>>> {
        &self._adj_list
    }

    fn add_edge(&mut self, node_1: GraphNode<T>, node_2: GraphNode<T>) {
        self._adj_list.get_mut(&node_1).unwrap().push(node_2);
    }

    fn does_contain_cycle(&self) -> bool {
        false
    }
}
