from algorithms.graph import UndirectedGraph, DirectedGraph, find_dsu, union_dsu


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


def test_find_dsu():
    parent = [-1, 4, 1, 2, -1]
    assert find_dsu(0, parent) == 0
    assert find_dsu(3, parent) == 4
    assert parent == [-1, 4, 4, 4, -1]


def test_union_dsu():
    parent = [-1, 4, 1, 2, -1]
    union_dsu(3, 0, parent)
    assert find_dsu(0, parent) == 4
    assert find_dsu(3, parent) == 4
    assert parent == [4, 4, 4, 4, -1]


def test_get_minimum_spanning_tree():
    edges = [
        (0, 1, 10),
        (0, 2, 12),
        (1, 2, 9),
        (1, 3, 8),
        (2, 4, 3),
        (2, 5, 1),
        (3, 4, 7),
        (3, 5, 10),
        (3, 6, 8),
        (3, 7, 5),
        (4, 5, 3),
        (5, 7, 6),
        (6, 7, 9),
        (6, 8, 2),
        (7, 8, 11),
    ]
    graph = UndirectedGraph(edges)
    mst_edges = {
        (2, 5, 1),
        (6, 8, 2),
        (4, 5, 3),
        (3, 7, 5),
        (1, 3, 8),
        (0, 1, 10),
        (3, 6, 8),
        (5, 7, 6),
    }
    assert len(mst_edges) == 8
    assert all([edge in mst_edges for edge in graph.get_minimum_spanning_tree()])


def test_shortest_path_dijkstra():
    edges = [
        (0, 1, 10),
        (0, 2, 5),
        (1, 2, 3),
        (1, 3, 8),
        (2, 4, 3),
        (2, 5, 1),
        (3, 4, 7),
        (3, 5, 10),
        (3, 6, 8),
        (3, 7, 5),
        (4, 5, 3),
        (5, 7, 6),
        (6, 7, 9),
        (6, 8, 2),
        (7, 8, 11),
    ]
    graph = UndirectedGraph(edges)
    assert graph.get_shortest_path_dijkstra(0, 1) == 8
    assert graph.get_shortest_path_dijkstra(0, 2) == 5
    assert graph.get_shortest_path_dijkstra(0, 3) == 15
    assert graph.get_shortest_path_dijkstra(0, 8) == 23


def test_shortest_path_bellman_ford_with_positive_edges():
    edges = [
        (0, 1, 10),
        (0, 2, 5),
        (1, 2, 3),
        (1, 3, 8),
        (2, 4, 3),
        (2, 5, 1),
        (3, 4, 7),
        (3, 5, 10),
        (3, 6, 8),
        (3, 7, 5),
        (4, 5, 3),
        (5, 7, 6),
        (6, 7, 9),
        (6, 8, 2),
        (7, 8, 11),
    ]
    graph = UndirectedGraph(edges)
    assert graph.get_shortest_path_bellman_ford(0, 1) == 8
    assert graph.get_shortest_path_bellman_ford(0, 2) == 5
    assert graph.get_shortest_path_bellman_ford(0, 3) == 15
    assert graph.get_shortest_path_bellman_ford(0, 8) == 23

def test_shortest_path_bellman_ford_with_positive_edges():
    edges = [
        (0, 1, 10),
        (0, 2, 5),
        (1, 2, 3),
        (1, 3, 8),
        (2, 4, 3),
        (2, 5, -1),
        (3, 4, 7),
        (3, 5, 10),
        (3, 6, 8),
        (3, 7, 5),
        (4, 5, 3),
        (5, 7, -1),
        (6, 7, 9),
        (6, 8, 2),
        (7, 8, 11),
    ]
    graph = DirectedGraph(edges)
    assert graph.get_shortest_path_bellman_ford(0, 1) == 10
    assert graph.get_shortest_path_bellman_ford(0, 2) == 5
    assert graph.get_shortest_path_bellman_ford(0, 3) == 18
    assert graph.get_shortest_path_bellman_ford(0, 8) == 14