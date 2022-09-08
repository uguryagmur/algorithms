from .abstract_graph import AbstractGraph
from typing import Dict, Hashable, Iterable, List, Optional, Set, Tuple


class UndirectedGraph(AbstractGraph):
    def add_edge(self, node_1: Hashable, node_2: Hashable, weight: float = 1.0) -> None:
        if self.adj_list.get(node_1, False):
            self.adj_list[node_1].add((node_2, float(weight)))
        else:
            self.adj_list[node_1] = {(node_2, float(weight))}
        self.visited[node_1] = False

        if self.adj_list.get(node_2, False):
            self.adj_list[node_2].add((node_1, float(weight)))
        else:
            self.adj_list[node_2] = {(node_1, float(weight))}
        self.visited[node_2] = False

    def does_contain_cycle(
        self, source: Hashable, parent: Optional[Hashable] = None
    ) -> bool:
        self.visited[source] = True
        for node, _ in self.adj_list.get(source, []):
            if not self.visited[node]:
                if self.does_contain_cycle(node, source):
                    return True
            elif node != parent:
                return True
        return False

    def get_shortest_path_bellman_ford(self, start: Hashable, end: Hashable) -> float:
        return super().get_shortest_path_bellman_ford(start, end, False)