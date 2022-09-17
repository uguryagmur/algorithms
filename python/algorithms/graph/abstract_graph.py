from abc import ABC, abstractmethod
from typing import Dict, Iterable, Hashable, List, Optional, Set, Tuple, Union

from .util import find_dsu, union_dsu


class AbstractGraph(ABC):
    def __init__(
        self,
        edges: Optional[
            Union[
                Iterable[Tuple[Hashable, Hashable, float]],
                Iterable[Tuple[Hashable, Hashable]],
            ]
        ],
    ) -> None:
        self.adj_list: Dict[Hashable, Set[Tuple[Hashable, float]]] = dict()
        self.visited: Dict[Hashable, bool] = dict()
        if edges:
            for edge in edges:
                self.add_edge(*edge)

    @abstractmethod
    def add_edge(self, node_1: Hashable, node_2: Hashable) -> None:
        raise NotImplementedError

    def clean_visited(self) -> None:
        for key in self.visited:
            self.visited[key] = False

    def get_edges(self) -> Set[Tuple[Hashable, Hashable]]:
        edges: Set[Tuple[Hashable, Hashable]] = set()
        for source, neighbours in self.adj_list.items():
            for node, weight in neighbours:
                edges.add((min(source, node), max(source, node), weight))
        return edges

    def dfs(
        self, source: Hashable, traverse_list: Optional[List[Hashable]] = None
    ) -> List[Hashable]:
        if traverse_list is None:
            traverse_list = list()

        self.visited[source] = True
        traverse_list.append(source)
        for node, _ in self.adj_list[source]:
            if not self.visited[node]:
                self.dfs(node, traverse_list)
        return traverse_list

    def bfs(self, source: Hashable) -> List[Hashable]:
        self.clean_visited()
        traverse_list: List[Hashable] = list()
        queue: List[Hashable] = list()
        queue.append(source)

        while queue:
            if not self.visited[queue[0]]:
                self.visited[queue[0]] = True
                for e, _ in self.adj_list[queue[0]]:
                    queue.append(e)
                traverse_list.append(queue[0])
            queue.pop(0)

        return traverse_list

    def is_bipartite(
        self,
        source: Hashable,
        parent_color: int = 2,
        color_list: Optional[Dict[Hashable, int]] = None,
    ) -> bool:
        # for color list 0 -> unvisited, 1 -> color 1, 2 -> color 2
        if color_list is None:
            color_list = {k: 0 for k in self.adj_list}

        color_list[source] = 3 - parent_color
        for node, _ in self.adj_list[source]:
            if color_list[node] == 0:
                if not self.is_bipartite(node, color_list[source], color_list):
                    return False

            elif color_list[node] == color_list[source]:
                return False

        return True

    def get_minimum_spanning_tree(self):
        edges: List[Tuple[Hashable, Hashable, float]] = list(self.get_edges())
        parent: List[int] = [-1 for _ in self.adj_list]
        edges.sort(key=lambda x: x[2])
        mst_edges: List[Tuple[Hashable, Hashable, float]] = list()
        for edge in edges:
            if find_dsu(edge[0], parent) != find_dsu(edge[1], parent):
                mst_edges.append(edge)
                union_dsu(edge[0], edge[1], parent)
        return mst_edges

    def get_shortest_path_dijkstra(self, start: Hashable, end: Hashable) -> float:
        self.clean_visited()
        distances: Dict[Hashable, float] = {node: -1 for node in self.adj_list}
        queue: List[Hashable] = [start]
        distances[start] = 0
        self.visited[start] = True
        while queue:
            source = queue[0]
            for node, weight in self.adj_list[source]:
                if not self.visited[node]:
                    queue.append(node)
                    self.visited[node] = True
                if (
                    distances[node] == -1
                    or weight + distances[source] < distances[node]
                ):
                    distances[node] = weight + distances[source]
            queue.pop(0)
        return distances[end] if distances[end] != -1 else float("inf")

    def get_shortest_path_bellman_ford(
        self, start: Hashable, end: Hashable, is_directed: bool
    ) -> float:
        edges: List[Tuple[Hashable, Hashable, float]] = self.get_edges()
        distances: Dict[Hashable, float] = {key: float("inf") for key in self.adj_list}
        distances[start] = 0
        for _ in range(len(self.adj_list) - 1):
            for edge in edges:
                s, d, w = edge
                if distances[s] != float("inf") and distances[s] + w < distances[d]:
                    distances[d] = distances[s] + w
                if not is_directed:
                    if distances[d] != float("inf") and distances[d] + w < distances[s]:
                        distances[s] = distances[d] + w
        return distances[end]

    def get_all_shortest_paths_floyd_marshall(
        self, is_directed: bool
    ) -> List[List[float]]:
        n: int = len(self.adj_list)
        distances: List[List[float]] = [
            [float("inf") for _ in range(n)] for _ in range(n)
        ]
        for edge in self.get_edges():
            distances[edge[0]][edge[1]] = edge[2]
            if not is_directed:
                distances[edge[1]][edge[0]] = edge[2]
        for i in range(n):
            distances[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if distances[i][j] > distances[i][k] + distances[k][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]

                    if not is_directed:
                        if distances[j][i] > distances[j][k] + distances[k][i]:
                            distances[j][i] = distances[j][k] + distances[k][i]

        return distances
