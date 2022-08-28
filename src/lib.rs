pub mod graph;

#[cfg(test)]
mod undirected_graph_tests {
    use crate::graph::functions;
    use crate::graph::structs;
    use crate::graph::structs::GraphNode;
    use crate::graph::traits::Graph;
    use std::ops::Deref;

    #[test]
    fn test_cycle_detection() {
        let n0 = GraphNode::create_with_id(0);
        let n1 = GraphNode::create_with_id(1);
        let n2 = GraphNode::create_with_id(2);
        let n3 = GraphNode::create_with_id(3);
        let n4 = GraphNode::create_with_id(4);
        let n5 = GraphNode::create_with_id(5);
        let edges = [(&n0, &n1), (&n0, &n2), (&n1, &n3), (&n1, &n5), (&n2, &n4)];
        let mut graph = Box::new(structs::UndirectedGraph::new(&edges));
        assert_eq!(graph.does_contain_cycle(), false);
        graph.add_edge(n4, n5);
        assert_eq!(graph.does_contain_cycle(), true);
    }

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
        assert_eq!(
            functions::dfs(graph.deref(), &n0),
            [0, 1, 3, 5, 4, 2].to_vec()
        );
        assert_eq!(
            functions::dfs(graph.deref(), &n1),
            [1, 0, 2, 4, 5, 3].to_vec()
        );
    }

    #[test]
    fn test_bfs() {
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
        assert_eq!(
            functions::bfs(graph.deref(), &n0),
            [0, 1, 2, 3, 5, 4].to_vec()
        );
        assert_eq!(
            functions::bfs(graph.deref(), &n1),
            [1, 0, 3, 5, 2, 4].to_vec()
        );
    }
}

#[cfg(test)]
mod directed_graph_tests {
    use crate::graph::functions;
    use crate::graph::structs;
    use crate::graph::structs::GraphNode;
    use crate::graph::traits::Graph;
    use std::ops::Deref;

    #[test]
    fn test_cycle_detection() {
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
        let mut graph = Box::new(structs::DirectedGraph::new(&edges));
        assert_eq!(graph.does_contain_cycle(), false);
        graph.add_edge(n5, n2);
        assert_eq!(graph.does_contain_cycle(), true);
    }

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
        let graph = Box::new(structs::DirectedGraph::new(&edges));
        assert_eq!(
            functions::dfs(graph.deref(), &n0),
            [0, 1, 3, 5, 2, 4].to_vec()
        );
        assert_eq!(functions::dfs(graph.deref(), &n1), [1, 3, 5].to_vec());
    }

    #[test]
    fn test_bfs() {
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
        let graph = Box::new(structs::DirectedGraph::new(&edges));
        assert_eq!(
            functions::bfs(graph.deref(), &n0),
            [0, 1, 2, 3, 5, 4].to_vec()
        );
        assert_eq!(functions::bfs(graph.deref(), &n1), [1, 3, 5].to_vec());
    }
}
