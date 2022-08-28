use super::structs::GraphNode;
use super::traits::Graph;
use std::collections::HashMap;

pub fn dfs<T: Copy + Eq + std::hash::Hash>(
    graph: &impl Graph<T>,
    source: &GraphNode<T>,
) -> Vec<usize> {
    let mut traverse_array: Vec<usize> = Vec::new();
    let mut visited: HashMap<GraphNode<T>, bool> = HashMap::new();
    for node in graph.get_adj_list().keys() {
        visited.insert(*node, false);
    }
    dfs_util(graph, source, &mut visited, &mut traverse_array);
    traverse_array
}

fn dfs_util<T: Copy + Eq + std::hash::Hash>(
    graph: &impl Graph<T>,
    source: &GraphNode<T>,
    visited: &mut HashMap<GraphNode<T>, bool>,
    traverse_array: &mut Vec<usize>,
) {
    visited.insert(*source, true);
    traverse_array.push(source._id);
    for node in graph.get_adj_list().get(source).unwrap() {
        if !visited.get(node).unwrap() {
            dfs_util(graph, node, visited, traverse_array);
        }
    }
}
