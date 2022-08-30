pub mod graph;

#[cfg(test)]
mod undirected_graph_tests {
    use crate::graph::functions;
    use crate::graph::structs;
    use crate::graph::structs::GraphNode;
    use crate::graph::traits::Graph;
    use std::ops::Deref;

    static N0: GraphNode<usize> = GraphNode::create_with_id(0);
    static N1: GraphNode<usize> = GraphNode::create_with_id(1);
    static N2: GraphNode<usize> = GraphNode::create_with_id(2);
    static N3: GraphNode<usize> = GraphNode::create_with_id(3);
    static N4: GraphNode<usize> = GraphNode::create_with_id(4);
    static N5: GraphNode<usize> = GraphNode::create_with_id(5);

    #[test]
    fn test_cycle_detection() {
        let edges = [(&N0, &N1), (&N0, &N2), (&N1, &N3), (&N1, &N5), (&N2, &N4)];
        let mut graph = Box::new(structs::UndirectedGraph::new(&edges));
        assert_eq!(graph.does_contain_cycle(), false);
        graph.add_edge(N4, N5);
        assert_eq!(graph.does_contain_cycle(), true);
    }

    #[test]
    fn test_dfs() {
        let edges = [
            (&N0, &N1),
            (&N0, &N2),
            (&N1, &N3),
            (&N1, &N5),
            (&N2, &N4),
            (&N4, &N5),
        ];
        let graph = Box::new(structs::UndirectedGraph::new(&edges));
        assert_eq!(
            functions::dfs(graph.deref(), &N0),
            [0, 1, 3, 5, 4, 2].to_vec()
        );
        assert_eq!(
            functions::dfs(graph.deref(), &N1),
            [1, 0, 2, 4, 5, 3].to_vec()
        );
    }

    #[test]
    fn test_bfs() {
        let edges = [
            (&N0, &N1),
            (&N0, &N2),
            (&N1, &N3),
            (&N1, &N5),
            (&N2, &N4),
            (&N4, &N5),
        ];
        let graph = Box::new(structs::UndirectedGraph::new(&edges));
        assert_eq!(
            functions::bfs(graph.deref(), &N0),
            [0, 1, 2, 3, 5, 4].to_vec()
        );
        assert_eq!(
            functions::bfs(graph.deref(), &N1),
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

    static N0: GraphNode<usize> = GraphNode::create_with_id(0);
    static N1: GraphNode<usize> = GraphNode::create_with_id(1);
    static N2: GraphNode<usize> = GraphNode::create_with_id(2);
    static N3: GraphNode<usize> = GraphNode::create_with_id(3);
    static N4: GraphNode<usize> = GraphNode::create_with_id(4);
    static N5: GraphNode<usize> = GraphNode::create_with_id(5);

    #[test]
    fn test_cycle_detection() {
        let edges = [
            (&N0, &N1),
            (&N0, &N2),
            (&N1, &N3),
            (&N1, &N5),
            (&N2, &N4),
            (&N4, &N5),
        ];
        let mut graph = Box::new(structs::DirectedGraph::new(&edges));
        assert_eq!(graph.does_contain_cycle(), false);
        graph.add_edge(N5, N2);
        assert_eq!(graph.does_contain_cycle(), true);
    }

    #[test]
    fn test_dfs() {
        let edges = [
            (&N0, &N1),
            (&N0, &N2),
            (&N1, &N3),
            (&N1, &N5),
            (&N2, &N4),
            (&N4, &N5),
        ];
        let graph = Box::new(structs::DirectedGraph::new(&edges));
        assert_eq!(
            functions::dfs(graph.deref(), &N0),
            [0, 1, 3, 5, 2, 4].to_vec()
        );
        assert_eq!(functions::dfs(graph.deref(), &N1), [1, 3, 5].to_vec());
    }

    #[test]
    fn test_bfs() {
        let edges = [
            (&N0, &N1),
            (&N0, &N2),
            (&N1, &N3),
            (&N1, &N5),
            (&N2, &N4),
            (&N4, &N5),
        ];
        let graph = Box::new(structs::DirectedGraph::new(&edges));
        assert_eq!(
            functions::bfs(graph.deref(), &N0),
            [0, 1, 2, 3, 5, 4].to_vec()
        );
        assert_eq!(functions::bfs(graph.deref(), &N1), [1, 3, 5].to_vec());
    }

    #[test]
    fn test_topological_sort() {
        let edges = [
            (&N0, &N2),
            (&N1, &N2),
            (&N1, &N4),
            (&N2, &N3),
            (&N3, &N5),
            (&N4, &N5),
        ];
        let graph = structs::DirectedGraph::new(&edges);
        let topological_sort_array = functions::sort_topologically(&graph);
        let correct_result = topological_sort_array == [0, 1, 2, 4, 3, 5].to_vec()
            || topological_sort_array == [1, 0, 4, 2, 3, 5].to_vec();
        assert_eq!(correct_result, true);
    }
}
