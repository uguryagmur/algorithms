use super::structs::GraphNode;
use std::collections::HashMap;

pub trait Graph<T> {
    fn new(edges: &[(&GraphNode<T>, &GraphNode<T>)]) -> Self;
    fn get_adj_list(&self) -> &HashMap<GraphNode<T>, Vec<GraphNode<T>>>;
    fn add_edge(&mut self, node_1: GraphNode<T>, node_2: GraphNode<T>);
    fn does_contain_cycle(&self) -> bool;
}
