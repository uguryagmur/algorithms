from operator import index
from re import L
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple


class UndirectedGraph:

    def __init__(self, edges: Optional[Iterable[Tuple[Any, Any]]]) -> None:
        self.adj_list: Dict[Any, Set[Any]] = dict()
        self.visited: Dict[Any, bool] = dict()
        if edges:
            for edge in edges:
                self.add_edge(*edge)
        
    def add_edge(self, node_1: Any, node_2: Any) -> None:
        if self.adj_list.get(node_1, False):
            self.adj_list[node_1].add(node_2)
        else:
            self.adj_list[node_1] = {node_2}
        self.visited[node_1] = False

        if self.adj_list.get(node_2, False):
            self.adj_list[node_2].add(node_1)
        else:
            self.adj_list[node_2] = {node_1}
        self.visited[node_2] = False
    
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
