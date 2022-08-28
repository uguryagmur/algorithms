pub mod graph;

#[cfg(test)]
mod undirected_graph_tests {
    use std::ops::Deref;
    use crate::graph::functions;
    use crate::graph::structs;
    use crate::graph::structs::GraphNode;
    use crate::graph::traits::Graph;

    #[test]
    fn test_dfs() {
        let n0 = GraphNode::create_with_id(0);
        let n1 = GraphNode::create_with_id(1);
        let n2 = GraphNode::create_with_id(2);
        let n3 = GraphNode::create_with_id(3);
        let n4 = GraphNode::create_with_id(4);
        let n5 = GraphNode::create_with_id(5);
        let edges = [
            (&n0, &n1),
            (&n0, &n2),
            (&n1, &n3),
            (&n1, &n5),
            (&n2, &n4),
            (&n4, &n5),
        ];
        let graph = Box::new(structs::UndirectedGraph::new(&edges));
        assert_eq!(functions::dfs(graph.deref(), &n0), [0, 1, 3, 5, 4, 2].to_vec());
    }
}
