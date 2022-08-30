use super::structs::{DirectedGraph, GraphNode};
use super::traits::Graph;
use std::collections::{HashMap, VecDeque};

pub fn sort_topologically<T>(graph: &DirectedGraph<T>) -> Vec<usize>
where
    T: Copy + Eq + std::hash::Hash,
{
    let mut queue: VecDeque<&GraphNode<T>> = VecDeque::new();
    let mut dependency_nums: HashMap<&GraphNode<T>, isize> = HashMap::new();
    let mut traverse_order: Vec<usize> = Vec::new();
    for node in graph.get_adj_list().keys() {
        dependency_nums.insert(node, 0);
    }
    for node_list in graph.get_adj_list().values() {
        for node in node_list {
            *dependency_nums.get_mut(node).unwrap() += 1;
        }
    }
    for (node, num_depends) in &dependency_nums {
        if *num_depends == 0 {
            queue.push_back(*node);
        }
    }
    while !queue.is_empty() {
        for node in graph.get_adj_list().get(queue[0]).unwrap() {
            *dependency_nums.get_mut(node).unwrap() -= 1;
            if *dependency_nums.get(node).unwrap() == 0 {
                queue.push_back(node);
            }
        }
        traverse_order.push(queue.pop_front().unwrap()._id);
    }
    traverse_order
}

pub fn bfs<T>(graph: &impl Graph<T>, source: &GraphNode<T>) -> Vec<usize>
where
    T: Copy + Eq + std::hash::Hash,
{
    let mut traverse_array: Vec<usize> = Vec::new();
    let mut visited: HashMap<GraphNode<T>, bool> = HashMap::new();
    for node in graph.get_adj_list().keys() {
        visited.insert(*node, false);
    }
    let mut queue = VecDeque::new();
    queue.push_back(source);
    while !queue.is_empty() {
        visited.insert(*queue[0], true);

        for node in graph.get_adj_list().get(queue[0]).unwrap() {
            if !visited.get(node).unwrap() {
                visited.insert(*node, true);
                queue.push_back(node);
            }
        }

        traverse_array.push(queue.pop_front().unwrap()._id);
    }
    traverse_array
}

pub fn dfs<T>(graph: &impl Graph<T>, source: &GraphNode<T>) -> Vec<usize>
where
    T: Copy + Eq + std::hash::Hash,
{
    let mut traverse_array: Vec<usize> = Vec::new();
    let mut visited: HashMap<GraphNode<T>, bool> = HashMap::new();
    for node in graph.get_adj_list().keys() {
        visited.insert(*node, false);
    }
    dfs_util(graph, source, &mut visited, &mut traverse_array);
    traverse_array
}

fn dfs_util<T>(
    graph: &impl Graph<T>,
    source: &GraphNode<T>,
    visited: &mut HashMap<GraphNode<T>, bool>,
    traverse_array: &mut Vec<usize>,
) where
    T: Copy + Eq + std::hash::Hash,
{
    visited.insert(*source, true);
    traverse_array.push(source._id);
    for node in graph.get_adj_list().get(source).unwrap() {
        if !visited.get(node).unwrap() {
            dfs_util(graph, node, visited, traverse_array);
        }
    }
}
