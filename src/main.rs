use graph::UndirectedGraph;

use crate::graph::GraphNode;

pub mod binary_search_tree;
pub mod binary_tree;
pub mod graph;
mod tests {
    mod test_binary_search_tree;
    mod test_binary_tree;
}

fn main() {
    let g0 = GraphNode::create_with_id(0);
    let g1 = GraphNode::create_with_id(1);
    let g2 = GraphNode::create_with_id(2);
    let g3 = GraphNode::create_with_id(3);
    let g4 = GraphNode::create_with_id(4);
    let g5 = GraphNode::create_with_id(5);
    let g6 = GraphNode::create_with_id(6);
    let mut graph = UndirectedGraph::new_from_graph_node_vector([g0, g1, g2, g3, g4, g5, g6].to_vec());
    let edges = [(&g0, &g1), (&g0, &g2), (&g1, &g3), (&g2, &g4), (&g3, &g4)];
    graph.add_edges(&edges);
    graph.dfs(&g0);
}
