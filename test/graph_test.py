from algorithms.graph import UndirectedGraph, DirectedGraph


def test_undirected_graph_creation_with_edges():
    edges = [(0, 1), (0, 2), (1, 3), (1, 5), (2, 4), (4, 5)]
    graph = UndirectedGraph(edges)

    assert graph.adj_list == {
        0: {1, 2},
        1: {0, 3, 5},
        2: {0, 4},
        3: {1},
        4: {2, 5},
        5: {1, 4},
    }


def test_directed_graph_creation_with_edges():
    edges = [(0, 1), (0, 2), (1, 3), (1, 5), (2, 4), (4, 5)]
    graph = DirectedGraph(edges)

    assert graph.adj_list == {0: {1, 2}, 1: {3, 5}, 2: {4}, 3: {}, 4: {5}, 5: {}}


def test_undirected_graph_add_edge():
    edges = [(0, 1), (0, 2), (1, 3), (1, 5), (2, 4)]
    graph = UndirectedGraph(edges)

    assert graph.adj_list == {
        0: {1, 2},
        1: {0, 3, 5},
        2: {0, 4},
        3: {1},
        4: {2},
        5: {1},
    }

    graph.add_edge(4, 5)
    assert graph.adj_list == {
        0: {1, 2},
        1: {0, 3, 5},
        2: {0, 4},
        3: {1},
        4: {2, 5},
        5: {1, 4},
    }


def test_directed_graph_add_edge():
    edges = [(0, 1), (0, 2), (1, 3), (1, 5), (2, 4)]
    graph = DirectedGraph(edges)

    assert graph.adj_list == {0: {1, 2}, 1: {3, 5}, 2: {4}, 3: {}, 4: {}, 5: {}}

    graph.add_edge(4, 5)
    assert graph.adj_list == {0: {1, 2}, 1: {3, 5}, 2: {4}, 3: {}, 4: {5}, 5: {}}


def test_undirected_graph_dfs():
    edges = [(0, 1), (0, 2), (1, 3), (1, 5), (2, 4), (4, 5)]
    graph = UndirectedGraph(edges)
    assert graph.dfs(0) == [0, 1, 3, 5, 4, 2]
    graph.clean_visited()
    assert graph.dfs(1) == [1, 0, 2, 4, 5, 3]


def test_directed_graph_dfs():
    edges = [(0, 1), (0, 2), (1, 3), (1, 5), (2, 4), (4, 5)]
    graph = DirectedGraph(edges)
    assert graph.dfs(0) == [0, 1, 3, 5, 2, 4]
    graph.clean_visited()
    assert graph.dfs(1) == [1, 3, 5]


def test_undirected_graph_bfs():
    edges = [(0, 1), (0, 2), (1, 3), (1, 5), (2, 4), (4, 5)]
    graph = UndirectedGraph(edges)
    assert graph.bfs(0) == [0, 1, 2, 3, 5, 4]
    graph.clean_visited()
    assert graph.bfs(1) == [1, 0, 3, 5, 2, 4]


def test_directed_graph_bfs():
    edges = [(0, 1), (0, 2), (1, 3), (1, 5), (2, 4), (4, 5)]
    graph = DirectedGraph(edges)
    assert graph.bfs(0) == [0, 1, 2, 3, 5, 4]
    graph.clean_visited()
    assert graph.bfs(1) == [1, 3, 5]
