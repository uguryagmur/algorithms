from .abstract_graph import AbstractGraph
from typing import Dict, Hashable, Iterable, List, Optional, Set, Tuple


class DirectedGraph(AbstractGraph):
    def add_edge(self, node_1: Hashable, node_2: Hashable, weight: float = 1.0) -> None:
        if self.adj_list.get(node_1, False):
            self.adj_list[node_1].add((node_2, float(weight)))
        else:
            self.adj_list[node_1] = {(node_2, float(weight))}
        self.visited[node_1] = False

        if self.adj_list.get(node_2, None) is None:
            self.adj_list[node_2] = {}
        self.visited[node_2] = False

    def does_contain_cycle(
        self,
        source: Hashable,
        parent: Optional[Hashable] = None,
        stack: Optional[Set[Hashable]] = None,
    ) -> bool:
        if stack is None:
            stack = set()

        self.visited[source] = True
        stack.add(source)
        for node, _ in self.adj_list.get(source, []):
            if not self.visited[node]:
                if self.does_contain_cycle(node, source, stack):
                    return True
            elif node != parent and node in stack:
                return True
        stack.remove(source)
        return False

    def sort_topologically(self) -> List[Hashable]:
        if self.does_contain_cycle(list(self.adj_list.keys())[0]):
            raise RuntimeError("graph contains cycle, topological sort is not possible")
        self.clean_visited()

        num_depends = {k: 0 for k in self.adj_list}
        for neighbours in self.adj_list.values():
            for node, _ in neighbours:
                num_depends[node] += 1

        topologic_sort_array: List[Hashable] = list()
        queue: List[Hashable] = list()

        for node, num_depend in num_depends.items():
            if num_depend == 0:
                self.visited[node] = True
                queue.append(node)

        while queue:
            for node, _ in self.adj_list[queue[0]]:
                num_depends[node] -= 1

            topologic_sort_array.append(queue.pop(0))

            for node, num_depend in num_depends.items():
                if num_depend == 0 and not self.visited[node]:
                    self.visited[node] = True
                    queue.append(node)

        return topologic_sort_array

    def get_shortest_path_bellman_ford(self, start: Hashable, end: Hashable) -> float:
        return super().get_shortest_path_bellman_ford(start, end, True)

    def get_all_shortest_paths_floyd_marshall(self) -> List[List[float]]:
        return super().get_all_shortest_paths_floyd_marshall(True)
