from abc import ABC, abstractmethod
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple


class AbstractGraph(ABC):
    def __init__(self, edges: Optional[Iterable[Tuple[Any, Any]]]) -> None:
        self.adj_list: Dict[Any, Set[Any]] = dict()
        self.visited: Dict[Any, bool] = dict()
        if edges:
            for edge in edges:
                self.add_edge(*edge)

    @abstractmethod
    def add_edge(self, node_1: Any, node_2: Any) -> None:
        raise NotImplementedError

    def clean_visited(self) -> None:
        for key in self.visited:
            self.visited[key] = False

    def dfs(self, source: Any, traverse_list: Optional[List[Any]] = None) -> List[Any]:
        if traverse_list is None:
            traverse_list = list()

        self.visited[source] = True
        traverse_list.append(source)
        for node in self.adj_list[source]:
            if not self.visited[node]:
                self.dfs(node, traverse_list)
        return traverse_list

    def bfs(self, source: Any) -> List[Any]:
        self.clean_visited()
        traverse_list: List[Any] = list()
        queue: List[Any] = list()
        queue.append(source)

        while queue:
            if not self.visited[queue[0]]:
                self.visited[queue[0]] = True
                for e in self.adj_list[queue[0]]:
                    queue.append(e)
                traverse_list.append(queue[0])
            queue.pop(0)

        return traverse_list
