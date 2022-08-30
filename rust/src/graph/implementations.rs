use super::structs::*;
use super::traits::Graph;
use std::collections::HashMap;

impl GraphNode<usize> {
    pub const fn create_with_id(data: usize) -> Self {
        Self {
            _id: data,
            _data: data,
        }
    }
}

impl<T> GraphNode<T> {
    pub const fn create(id: usize, data: T) -> Self {
        Self {
            _id: id,
            _data: data,
        }
    }
}

impl<T> UndirectedGraph<T>
where
    T: Eq + Copy + std::hash::Hash,
{
    fn does_contain_cycle_util(
        &self,
        source: GraphNode<T>,
        parent: Option<GraphNode<T>>,
        visited: &mut HashMap<GraphNode<T>, bool>,
    ) -> bool {
        visited.insert(source, true);
        for node in self._adj_list.get(&source).unwrap() {
            if !visited.get(node).unwrap() {
                if self.does_contain_cycle_util(*node, Some(source), visited) {
                    return true;
                }
            } else if parent.is_some() && node._id != parent.unwrap()._id {
                return true;
            }
        }
        false
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
        let mut visited = HashMap::new();
        for node in self._adj_list.keys() {
            visited.insert(*node, false);
        }
        let source = self._adj_list.keys().nth(0).unwrap();
        self.does_contain_cycle_util(*source, None, &mut visited)
    }
}

impl<T> DirectedGraph<T>
where
    T: Eq + Copy + std::hash::Hash,
{
    fn does_contain_cycle_util(
        &self,
        source: GraphNode<T>,
        parent: Option<GraphNode<T>>,
        visited: &mut HashMap<GraphNode<T>, bool>,
        stack: &mut Vec<usize>,
    ) -> bool {
        visited.insert(source, true);
        stack.push(source._id);
        for node in self._adj_list.get(&source).unwrap() {
            if !visited.get(node).unwrap() {
                if self.does_contain_cycle_util(*node, Some(source), visited, stack) {
                    return true;
                }
            } else if parent.is_some()
                && node._id != parent.unwrap()._id
                && stack.contains(&node._id)
            {
                return true;
            }
        }
        stack.pop();
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
        let mut visited = HashMap::new();
        for node in self._adj_list.keys() {
            visited.insert(*node, false);
        }
        let source = self._adj_list.keys().nth(0).unwrap();
        let mut stack: Vec<usize> = Vec::new();
        self.does_contain_cycle_util(*source, None, &mut visited, &mut stack)
    }
}
