use std::{collections::HashMap, hash::Hash};

#[derive(Eq, Clone, Copy, Hash, PartialEq, Debug)]
pub struct GraphNode<T> {
    _id: usize,
    _data: T,
}

impl GraphNode<usize> {
    pub fn create_with_id(data: usize) -> Self {
        Self { _id: data, _data: data }
    }
}

impl<T> GraphNode<T> {
    pub fn create(id: usize, data: T) -> Self {
        Self {_id: id, _data: data}
    }
}

#[derive(Debug)]
pub struct UndirectedGraph<T> {
    _adj_list: HashMap<GraphNode<T>, Vec<GraphNode<T>>>,
}

pub struct DirectedGraph<T> {
    _adj_list: HashMap<GraphNode<T>, Vec<GraphNode<T>>>,
}

pub trait Graph<T> {
    fn new(edges: &[(&GraphNode<T>, &GraphNode<T>)]) -> Self;
    fn get_adj_list(&self) -> &HashMap<GraphNode<T>, Vec<GraphNode<T>>>;
    fn add_edge(&mut self, node_1: GraphNode<T>, node_2: GraphNode<T>);
    fn does_contain_cycle(&self) -> bool;
}

impl<T> Graph<T> for UndirectedGraph<T> 
    where T: Eq + Copy + std::hash::Hash {

    fn new(edges: &[(&GraphNode<T>, &GraphNode<T>)]) -> Self {
        let mut adj_list: HashMap<GraphNode<T>, Vec<GraphNode<T>>> = HashMap::new();
        for edge in edges{
            if adj_list.get(&edge.0).is_none(){
                adj_list.insert(*edge.0, vec![*edge.1]);
            }
            else {
                adj_list.get_mut(&edge.0).unwrap().push(*edge.1);
            }

            if adj_list.get(&edge.1).is_none(){
                adj_list.insert(*edge.1, vec![*edge.0]);
            }
            else {
                adj_list.get_mut(&edge.1).unwrap().push(*edge.0);
            }
        }
        Self{_adj_list: adj_list}
    }

    fn get_adj_list(&self) -> &HashMap<GraphNode<T>, Vec<GraphNode<T>>> {
        &self._adj_list
    }

    fn add_edge(&mut self, node_1: GraphNode<T>, node_2: GraphNode<T>){
        self._adj_list.get_mut(&node_1).unwrap().push(node_2);
        self._adj_list.get_mut(&node_2).unwrap().push(node_1);
    }

    fn does_contain_cycle(&self) -> bool {
        false
    }
}


pub fn dfs<T: Copy + Eq + Hash>(graph: &impl Graph<T>, source: &GraphNode<T>) -> Vec<usize> {
    let mut traverse_array: Vec<usize> = Vec::new();
    let mut visited: HashMap<GraphNode<T>, bool> = HashMap::new();
    for node in graph.get_adj_list().keys() {
        visited.insert(*node, false);
    }
    dfs_util(graph, source, &mut visited, &mut traverse_array);
    traverse_array
}

fn dfs_util<T: Copy + Eq + Hash>(graph: &impl Graph<T>, source: &GraphNode<T>, visited: &mut HashMap<GraphNode<T>, bool>, traverse_array: &mut Vec<usize>) {
    visited.insert(*source, true);
    traverse_array.push(source._id);
    for node in graph.get_adj_list().get(source).unwrap(){
        if !visited.get(node).unwrap(){
            dfs_util(graph, node, visited, traverse_array);
        }
    }
}