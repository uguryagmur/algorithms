from algorithms.graph import UndirectedGraph, DirectedGraph


def test_undirected_graph_creation_with_edges():
    edges = [(0, 1), (0, 2), (1, 3, 6), (1, 5), (2, 4), (4, 5)]
    graph = UndirectedGraph(edges)

    assert graph.adj_list == {
        0: {(1, 1), (2, 1)},
        1: {(0, 1), (3, 6), (5, 1)},
        2: {(0, 1), (4, 1)},
        3: {(1, 6)},
        4: {(2, 1), (5, 1)},
        5: {(1, 1), (4, 1)},
    }


def test_directed_graph_creation_with_edges():
    edges = [(0, 1), (0, 2), (1, 3, 6), (1, 5), (2, 4), (4, 5)]
    graph = DirectedGraph(edges)

    assert graph.adj_list == {
        0: {(1, 1), (2, 1)},
        1: {(3, 6), (5, 1)},
        2: {(4, 1)},
        3: {},
        4: {(5, 1)},
        5: {},
    }


def test_undirected_graph_add_edge():
    edges = [(0, 1), (0, 2), (1, 3), (1, 5), (2, 4)]
    graph = UndirectedGraph(edges)

    assert graph.adj_list == {
        0: {(1, 1), (2, 1)},
        1: {(0, 1), (3, 1), (5, 1)},
        2: {(0, 1), (4, 1)},
        3: {(1, 1)},
        4: {(2, 1)},
        5: {(1, 1)},
    }

    graph.add_edge(4, 5, 9)
    assert graph.adj_list == {
        0: {(1, 1), (2, 1)},
        1: {(0, 1), (3, 1), (5, 1)},
        2: {(0, 1), (4, 1)},
        3: {(1, 1)},
        4: {(2, 1), (5, 9)},
        5: {(1, 1), (4, 9)},
    }


def test_directed_graph_add_edge():
    edges = [(0, 1), (0, 2), (1, 3), (1, 5), (2, 4)]
    graph = DirectedGraph(edges)

    assert graph.adj_list == {
        0: {(1, 1), (2, 1)},
        1: {(3, 1), (5, 1)},
        2: {(4, 1)},
        3: {},
        4: {},
        5: {},
    }

    graph.add_edge(4, 5, 9)
    assert graph.adj_list == {
        0: {(1, 1), (2, 1)},
        1: {(3, 1), (5, 1)},
        2: {(4, 1)},
        3: {},
        4: {(5, 9)},
        5: {},
    }


def test_undirected_graph_dfs():
    edges = [(0, 1), (0, 2), (1, 3), (1, 5), (2, 4), (4, 5)]
    graph = UndirectedGraph(edges)
    dfs_result = graph.dfs(0)
    assert dfs_result == [0, 1, 3, 5, 4, 2] or dfs_result == [0, 1, 5, 4, 2, 3]
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
    bfs_result = graph.bfs(0)
    assert bfs_result == [0, 1, 2, 3, 5, 4] or bfs_result == [0, 1, 2, 5, 3, 4]
    graph.clean_visited()
    bfs_result = graph.bfs(1)
    assert bfs_result == [1, 0, 3, 5, 2, 4] or bfs_result == [1, 0, 5, 3, 2, 4]


def test_directed_graph_bfs():
    edges = [(0, 1), (0, 2), (1, 3), (1, 5), (2, 4), (4, 5)]
    graph = DirectedGraph(edges)
    assert graph.bfs(0) == [0, 1, 2, 3, 5, 4]
    graph.clean_visited()
    assert graph.bfs(1) == [1, 3, 5]


def test_undirected_graph_cycle_detection():
    edges = [(0, 1), (0, 2), (1, 3), (1, 5), (2, 4)]
    graph = UndirectedGraph(edges)
    assert graph.does_contain_cycle(0) == False
    graph.add_edge(4, 5)
    graph.clean_visited()
    assert graph.does_contain_cycle(0) == True


def test_directed_graph_cycle_detection():
    edges = [(0, 1), (0, 2), (1, 3), (1, 5), (2, 4), (4, 5)]
    graph = DirectedGraph(edges)
    assert graph.does_contain_cycle(0) == False
    graph.add_edge(5, 2)
    graph.clean_visited()
    assert graph.does_contain_cycle(0) == True


def test_indirected_graph_is_bipartite():
    edges = [(0, 1), (0, 2), (1, 3), (2, 4), (4, 5)]
    graph = UndirectedGraph(edges)
    assert graph.is_bipartite(0) == True
    graph.add_edge(1, 5)
    assert graph.is_bipartite(0) == False


def test_directed_graph_is_bipartite():
    edges = [(0, 1), (0, 2), (1, 3), (2, 4), (4, 5)]
    graph = DirectedGraph(edges)
    assert graph.is_bipartite(0) == True
    graph.add_edge(1, 5)
    assert graph.is_bipartite(0) == False


def test_directed_graph_topological_sort():
    edges = [(0, 2), (1, 2), (1, 4), (2, 3), (3, 5), (4, 5)]
    graph = DirectedGraph(edges)
    graph.sort_topologically() == [0, 1, 2, 4, 3, 5]
