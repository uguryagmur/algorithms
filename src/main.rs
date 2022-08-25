use crate::graph::GraphNode;
use crate::graph::Graph;

pub mod binary_search_tree;
pub mod binary_tree;
pub mod graph;

fn main() {
    let g0 = GraphNode::create_with_id(0);
    let g1 = GraphNode::create_with_id(1);
    let g2 = GraphNode::create_with_id(2);
    let g3 = GraphNode::create_with_id(3);
    let g4 = GraphNode::create_with_id(4);
    let edges = [(&g0, &g1), (&g0, &g2), (&g1, &g3), (&g2, &g4), (&g3, &g4)];
    let graph = graph::UndirectedGraph::new(&edges);
    println!("{:?}", graph::dfs(&graph, &g0))
}
