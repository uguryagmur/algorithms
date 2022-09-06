from abc import ABC, abstractmethod
from typing import Dict, Iterable, Hashable, List, Optional, Set, Tuple, Union
from xml.dom import minicompat


class AbstractGraph(ABC):
    def __init__(
        self,
        edges: Optional[
            Union[
                Iterable[Tuple[Hashable, Hashable, int]],
                Iterable[Tuple[Hashable, Hashable]],
            ]
        ],
    ) -> None:
        self.adj_list: Dict[Hashable, Set[Tuple[Hashable, int]]] = dict()
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
