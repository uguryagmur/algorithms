from .abstract_graph import AbstractGraph
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple


class UndirectedGraph(AbstractGraph):
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
